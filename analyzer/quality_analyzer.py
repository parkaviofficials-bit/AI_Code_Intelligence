def calculate_quality_score(features):

    score = 100
    reasons = []

    # Complexity penalty
    complexity = features["cyclomatic_complexity"]

    if complexity > 10:
        score -= 25
        reasons.append("Very high cyclomatic complexity")
    elif complexity > 5:
        score -= 15
        reasons.append("High cyclomatic complexity")
    elif complexity > 3:
        score -= 8
        reasons.append("Moderate cyclomatic complexity")

    # Function size penalty
    avg_length = features["average_function_length"]

    if avg_length > 30:
        score -= 20
        reasons.append("Functions are too large")
    elif avg_length > 15:
        score -= 10
        reasons.append("Functions are relatively large")

    # Too many branches
    if features["if_statements"] > 10:
        score -= 10
        reasons.append("Many conditional branches")

    # Too many loops
    if features["loops"] > 5:
        score -= 10
        reasons.append("Many loops")

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    # Quality category
    if score >= 85:
        category = "Excellent"
    elif score >= 70:
        category = "Good"
    elif score >= 50:
        category = "Moderate"
    else:
        category = "Needs Improvement"

    return {
        "score": score,
        "category": category,
        "reasons": reasons
    }