from analyzer.feature_extractor import extract_features


def test_feature_extraction():
    features = extract_features("test_code/complex_sample.py")

    assert features["lines_of_code"] == 50
    assert features["functions"] == 4
    assert features["classes"] == 0
    assert features["if_statements"] == 11
    assert features["loops"] == 2
    assert features["returns"] == 5
    assert features["function_calls"] == 14
    assert features["imports"] == 1
    assert features["average_function_length"] == 14.75
    assert features["cyclomatic_complexity"] == 14