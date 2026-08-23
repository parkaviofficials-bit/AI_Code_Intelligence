from analyzer.security_analyzer import analyze_security


def test_security_analyzer():
    result = analyze_security("test_code/complex_sample.py")

    assert isinstance(result, list)