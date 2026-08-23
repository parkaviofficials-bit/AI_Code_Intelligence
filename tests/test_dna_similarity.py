from analyzer.dna_similarity import calculate_similarity


def test_dna_similarity():
    features_a = {
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

    features_b = features_a.copy()

    result = calculate_similarity(
        features_a,
        features_b
    )

    assert isinstance(result, (int, float))
    assert 0 <= result <= 100