from analyzer.quality_analyzer import calculate_quality_score


def test_quality_score():
    features = {
        "lines_of_code": 50,
        "functions": 4,
        "classes": 0,
        "if_statements": 11,
        "loops": 2,
        "returns": 5,
        "function_calls": 14,
        "imports": 1,
        "average_function_length": 14.75,
        "cyclomatic_complexity": 14,
    }

    result = calculate_quality_score(features)

    assert "score" in result
    assert "category" in result
    assert "reasons" in result

    assert 0 <= result["score"] <= 100