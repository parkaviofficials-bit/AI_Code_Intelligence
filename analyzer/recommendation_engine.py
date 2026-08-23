def generate_recommendations(features, security_issues, bug_risk):
    recommendations = []

    # ============================================================
    # CODE COMPLEXITY
    # ============================================================

    complexity = features.get("cyclomatic_complexity", 1)

    if complexity >= 10:
        recommendations.append({
            "type": "Complexity",
            "severity": "HIGH",
            "message": f"High cyclomatic complexity detected ({complexity}).",
            "recommendation": (
                "Break complex logic into smaller functions and "
                "simplify deeply nested conditional branches."
            )
        })

    elif complexity >= 5:
        recommendations.append({
            "type": "Complexity",
            "severity": "MEDIUM",
            "message": f"Moderate cyclomatic complexity detected ({complexity}).",
            "recommendation": (
                "Consider simplifying conditional logic and "
                "splitting complex functions."
            )
        })

    # ============================================================
    # FUNCTION LENGTH
    # ============================================================

    avg_length = features.get("average_function_length", 0)

    if avg_length >= 20:
        recommendations.append({
            "type": "Maintainability",
            "severity": "HIGH",
            "message": (
                f"Average function length is high ({avg_length:.1f} lines)."
            ),
            "recommendation": (
                "Split large functions into smaller, focused functions "
                "with clear responsibilities."
            )
        })

    elif avg_length >= 10:
        recommendations.append({
            "type": "Maintainability",
            "severity": "MEDIUM",
            "message": (
                f"Average function length is relatively high "
                f"({avg_length:.1f} lines)."
            ),
            "recommendation": (
                "Consider dividing longer functions into smaller "
                "reusable units."
            )
        })

    # ============================================================
    # FUNCTION STRUCTURE
    # ============================================================

    functions = features.get("functions", 0)
    lines_of_code = features.get("lines_of_code", 0)

    if functions == 0 and lines_of_code > 10:
        recommendations.append({
            "type": "Structure",
            "severity": "LOW",
            "message": "No functions were detected in the analyzed code.",
            "recommendation": (
                "Consider organizing repeated or logically related "
                "operations into reusable functions."
            )
        })

    # ============================================================
    # LARGE FILE
    # ============================================================

    if lines_of_code >= 300:
        recommendations.append({
            "type": "Maintainability",
            "severity": "HIGH",
            "message": f"The source file is large ({lines_of_code} lines).",
            "recommendation": (
                "Consider splitting the file into smaller modules "
                "with clearly defined responsibilities."
            )
        })

    elif lines_of_code >= 150:
        recommendations.append({
            "type": "Maintainability",
            "severity": "MEDIUM",
            "message": f"The source file is relatively large ({lines_of_code} lines).",
            "recommendation": (
                "Review the module structure and consider separating "
                "independent functionality."
            )
        })

    # ============================================================
    # LOOPS
    # ============================================================

    loops = features.get("loops", 0)

    if loops >= 5:
        recommendations.append({
            "type": "Complexity",
            "severity": "MEDIUM",
            "message": f"Multiple loops were detected ({loops}).",
            "recommendation": (
                "Review nested and repeated loops for unnecessary "
                "complexity and performance issues."
            )
        })

    # ============================================================
    # SECURITY
    # ============================================================

    if security_issues:
        recommendations.append({
            "type": "Security",
            "severity": "HIGH",
            "message": (
                f"{len(security_issues)} security issue(s) were detected."
            ),
            "recommendation": (
                "Review each security finding and remove unsafe "
                "patterns before deploying the application."
            )
        })

    # ============================================================
    # BUG RISK
    # ============================================================

    risk_level = bug_risk.get("risk_level", "LOW")

    if risk_level == "HIGH":
        recommendations.append({
            "type": "Bug Risk",
            "severity": "HIGH",
            "message": "The code has a high predicted bug risk.",
            "recommendation": (
                "Review complex logic, add comprehensive test cases, "
                "and inspect functions with high structural complexity."
            )
        })

    elif risk_level == "MEDIUM":
        recommendations.append({
            "type": "Bug Risk",
            "severity": "MEDIUM",
            "message": "The code has a moderate predicted bug risk.",
            "recommendation": (
                "Add test cases and carefully review conditional, "
                "looping, and complex logic."
            )
        })

    # ============================================================
    # POSITIVE RESULT
    # ============================================================

    if not recommendations:
        recommendations.append({
            "type": "Overall",
            "severity": "GOOD",
            "message": "No major improvement areas were detected.",
            "recommendation": (
                "The code currently shows good structural characteristics. "
                "Continue maintaining clear, modular, and secure code."
            )
        })

    return recommendations