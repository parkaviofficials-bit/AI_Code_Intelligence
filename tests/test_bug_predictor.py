from analyzer.bug_predictor import predict_bug_risk


def test_bug_prediction():
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

    result = predict_bug_risk(features)

    assert "prediction" in result
    assert "risk_probability" in result
    assert "risk_level" in result

    assert result["prediction"] in [0, 1]
    assert 0 <= float(result["risk_probability"]) <= 100
    assert result["risk_level"] in ["LOW", "MEDIUM", "HIGH"]