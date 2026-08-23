from analyzer.code_dna import generate_code_dna


def test_code_dna():
    features = {
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

    result = generate_code_dna(features)

    assert "dna_string" in result
    assert "fingerprint" in result

    assert isinstance(result["dna_string"], str)
    assert isinstance(result["fingerprint"], str)

    assert len(result["fingerprint"]) == 64