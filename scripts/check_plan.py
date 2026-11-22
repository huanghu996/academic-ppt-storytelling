#!/usr/bin/env python3
"""Check storyboard structure, not source truth, scientific inference, or presentation files. Standard library only."""

import argparse
import json
import math
from pathlib import Path
import sys


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def positive_number(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and value > 0
    )


def integer(value, minimum=0):
    return isinstance(value, int) and not isinstance(value, bool) and value >= minimum


def validate(plan):
    errors, warnings = [], []

    def error(code, where, message):
        errors.append({"code": code, "where": where, "message": message})

    def warn(code, where, message):
        warnings.append({"code": code, "where": where, "message": message})

    def require_text(obj, key, where):
        if not nonempty(obj.get(key)):
            error("TEXT_REQUIRED", where, f"{key} must be a nonempty string")

    def choice(obj, key, values, where):
        value = obj.get(key)
        if not isinstance(value, str) or value not in values:
            error("INVALID_CHOICE", where, f"{key} allowed values: {', '.join(sorted(values))}")

    if not isinstance(plan, dict):
        error("ROOT_OBJECT", "root", "The root must be a JSON object")
        return {"errors": errors, "warnings": warnings, "main_seconds": 0, "budget_seconds": None}

    if type(plan.get("schema_version")) is not int or plan["schema_version"] != 1:
        error("SCHEMA_VERSION", "root", "schema_version must be integer 1")
    choice(plan, "mode", {"research", "proposal", "progress", "review", "theory", "teaching"}, "root")
    require_text(plan, "main_message", "root")
    budget = plan.get("budget_seconds")
    if not positive_number(budget):
        error("INVALID_BUDGET", "root", "budget_seconds must be finite and positive")

    evidence = plan.get("evidence")
    if not isinstance(evidence, list):
        error("EVIDENCE_LIST", "root", "evidence must be a list; use an empty list when no evidence is available")
        evidence = []
    evidence_map = {}
    for i, item in enumerate(evidence, 1):
        where = f"evidence[{i}]"
        if not isinstance(item, dict):
            error("EVIDENCE_OBJECT", where, "Each evidence item must be an object")
            continue
        require_text(item, "id", where)
        require_text(item, "scope", where)
        choice(item, "kind", {"empirical", "literature", "derivation", "schematic"}, where)
        choice(item, "status", {"verified", "supplied", "missing", "illustrative"}, where)
        if item.get("status") in ("verified", "supplied"):
            require_text(item, "source", where)
        elif not isinstance(item.get("source"), str):
            error("SOURCE_TEXT", where, "source must be a string; missing or illustrative items may use an empty string")
        item_id = item.get("id")
        if nonempty(item_id):
            if item_id in evidence_map:
                error("DUPLICATE_EVIDENCE", where, f"Duplicate evidence ID: {item_id}")
            else:
                evidence_map[item_id] = item

    slides = plan.get("slides")
    if not isinstance(slides, list) or not slides:
        error("SLIDES_REQUIRED", "root", "slides must be a nonempty list")
        slides = []
    expected = plan.get("expected_total_slides")
    if "expected_total_slides" in plan:
        if not integer(expected, 1):
            error("INVALID_SLIDE_COUNT", "root", "expected_total_slides must be a positive integer")
        elif expected != len(slides):
            error("SLIDE_COUNT", "root", f"Actual entry count {len(slides)} differs from expected total {expected}")

    seen, main_seconds, main_count = set(), 0, 0
    for i, slide in enumerate(slides, 1):
        where = f"slides[{i}]"
        if not isinstance(slide, dict):
            error("SLIDE_OBJECT", where, "Each slide item must be an object")
            continue
        for key in ("id", "title", "role", "point", "visual", "transition"):
            require_text(slide, key, where)
        slide_id = slide.get("id")
        if nonempty(slide_id):
            if slide_id in seen:
                error("DUPLICATE_SLIDE", where, f"Duplicate slide ID: {slide_id}")
            seen.add(slide_id)
        choice(slide, "claim_type", {"setup", "question", "hypothesis", "plan", "finding", "interpretation", "limitation"}, where)
        is_main = slide.get("in_main")
        if not isinstance(is_main, bool):
            error("MAIN_FLAG", where, "in_main must be a boolean")
        seconds = slide.get("duration_seconds")
        if not positive_number(seconds):
            error("INVALID_DURATION", where, "duration_seconds must be finite and positive")
        if is_main is True:
            main_count += 1
            if positive_number(seconds):
                main_seconds += seconds
        if not isinstance(slide.get("boundary"), str):
            error("BOUNDARY_TEXT", where, "boundary must be a string; it may be empty when no specific limit applies")

        refs = slide.get("evidence_ids")
        if not isinstance(refs, list) or any(not nonempty(ref) for ref in refs):
            error("EVIDENCE_IDS", where, "evidence_ids must be a list of nonempty strings; the list may be empty")
            refs = []
        if len(refs) != len(set(refs)):
            warn("REPEATED_REFERENCE", where, "An evidence ID is repeated on the same slide")
        linked = []
        for ref in refs:
            if ref not in evidence_map:
                error("UNKNOWN_EVIDENCE", where, f"Unknown evidence ID: {ref}")
                continue
            item = evidence_map[ref]
            linked.append(item)
            if item.get("status") == "missing":
                warn("MISSING_EVIDENCE", where, f"{ref} is missing source material; mark this explicitly on the slide")
            elif item.get("status") == "supplied":
                warn("UNVERIFIED_SOURCE", where, f"{ref} is supplied but unchecked; this does not establish scientific verification")

        if slide.get("claim_type") in ("finding", "interpretation"):
            usable = [item for item in linked if item.get("status") in ("verified", "supplied")
                      and item.get("kind") in ("empirical", "literature", "derivation")
                      and nonempty(item.get("source"))]
            if not usable:
                error("CLAIM_WITHOUT_EVIDENCE", where, "A finding or interpretation needs at least one usable, nonillustrative source")
            if any(item.get("status") in ("missing", "illustrative")
                   or item.get("kind") == "schematic" for item in linked):
                error("NON_EVIDENCE_FOR_CLAIM", where, "Missing or illustrative items cannot support a finding/interpretation; describe them as visuals instead")
            if not nonempty(slide.get("boundary")):
                warn("CLAIM_SCOPE", where, "No scope is recorded for this finding/interpretation; inspect manually")

        animation = slide.get("animation")
        if not isinstance(animation, dict):
            error("ANIMATION_OBJECT", where, "animation must be an object; use mode=none for a static slide")
            continue
        choice(animation, "mode", {"none", "reveal", "highlight", "zoom", "physical-time"}, where)
        steps = animation.get("steps")
        if not integer(steps):
            error("ANIMATION_STEPS", where, "steps must be a nonnegative integer")
        elif animation.get("mode") == "none" and steps != 0:
            error("STATIC_STEPS", where, "A static slide must have steps=0")
        elif animation.get("mode") in ("reveal", "highlight", "zoom", "physical-time") and steps < 1:
            error("EMPTY_BUILD", where, "An animated slide needs at least one build or playback start")
        elif steps > 5:
            warn("MANY_BUILDS", where, "Many builds are planned; review reading and speaking pace")
        if not isinstance(animation.get("static_fallback"), str):
            error("FALLBACK_TEXT", where, "static_fallback must be a string")
        elif animation.get("mode") != "none" and not nonempty(animation["static_fallback"]):
            error("STATIC_FALLBACK", where, "An animated slide must explain how its static version preserves information")
        if animation.get("mode") == "physical-time":
            if not nonempty(animation.get("time_basis")):
                error("TIME_BASIS", where, "Real-time animation must state time units and sampling or playback information")

    if slides and main_count == 0:
        error("NO_MAIN_SLIDES", "root", "At least one main-talk slide is required")
    if positive_number(budget) and main_seconds > budget + 1e-6:
        error("OVER_BUDGET", "root", f"Main talk takes {main_seconds:g} seconds, above the {budget:g}-second budget")
    return {"errors": errors, "warnings": warnings, "main_seconds": main_seconds,
            "budget_seconds": budget if positive_number(budget) else None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="Structured storyboard JSON file")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable report")
    args = parser.parse_args()
    try:
        # utf-8-sig accepts UTF-8 with or without a Windows-style BOM.
        plan = json.loads(args.plan.read_text(encoding="utf-8-sig"),
                          parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"Invalid JSON numeric constant: {value}")))
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        report = {"errors": [{"code": "INPUT_ERROR", "where": str(args.plan), "message": str(exc)}],
                  "warnings": [], "main_seconds": None, "budget_seconds": None}
        code = 2
    else:
        report = validate(plan)
        code = 1 if report["errors"] else 0
    report["scope"] = "Structure only; source truth, scientific inference, layout, and actual playback are not verified"
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Structural check: {len(report['errors'])} blocker(s), {len(report['warnings'])} warning(s)")
        if report["main_seconds"] is not None:
            print(f"Main-talk time: {report['main_seconds']:g} seconds; budget: {report['budget_seconds']} seconds")
        for level in ("errors", "warnings"):
            for item in report[level]:
                print(f"[{level}/{item['code']}] {item['where']}: {item['message']}")
        print(report["scope"])
    return code


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
