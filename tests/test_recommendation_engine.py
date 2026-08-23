from analyzer.recommendation_engine import generate_recommendations


def test_recommendations():
    features = {
        "lines_of_code": 50,
        "functions": 4,
        "if_statements": 11,
        "loops": 2,
        "returns": 5,
        "function_calls": 14,
        "imports": 1,
        "average_function_length": 14.75,
        "cyclomatic_complexity": 14,
    }

    bug_risk = {
        "prediction": 1,
        "risk_probability": 64.33,
        "risk_level": "MEDIUM",
    }

    security_issues = []

    result = generate_recommendations(
        features,
        security_issues,
        bug_risk
    )

    assert isinstance(result, list)
    assert len(result) > 0

    types = [item["type"] for item in result]

    assert "Complexity" in types
    assert "Bug Risk" in types
    