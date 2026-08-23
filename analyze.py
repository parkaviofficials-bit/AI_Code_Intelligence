import sys

from analyzer.feature_extractor import extract_features
from analyzer.quality_analyzer import calculate_quality_score
from analyzer.security_analyzer import analyze_security
from analyzer.bug_predictor import predict_bug_risk
from analyzer.code_dna import generate_code_dna


def analyze_code(file_path):

    print("\n" + "=" * 60)
    print("           AI CODE INTELLIGENCE REPORT")
    print("=" * 60)

    print("\nFile:", file_path)

    # ==========================================
    # 1. FEATURE EXTRACTION
    # ==========================================

    features = extract_features(file_path)

    print("\nCODE METRICS")
    print("-" * 40)

    print("Lines of Code:", features["lines_of_code"])
    print("Functions:", features["functions"])
    print("Classes:", features["classes"])
    print("If Statements:", features["if_statements"])
    print("Loops:", features["loops"])
    print("Returns:", features["returns"])
    print("Function Calls:", features["function_calls"])
    print("Imports:", features["imports"])
    print(
        "Average Function Length:",
        features["average_function_length"]
    )
    print(
        "Cyclomatic Complexity:",
        features["cyclomatic_complexity"]
    )

    # ==========================================
    # 2. CODE QUALITY
    # ==========================================

    quality = calculate_quality_score(features)

    print("\nCODE QUALITY")
    print("-" * 40)

    print("Score:", quality["score"], "/ 100")
    print("Category:", quality["category"])

    if quality["reasons"]:

        print("\nQuality Issues:")

        for reason in quality["reasons"]:
            print("-", reason)

    else:
        print("No major quality issues detected.")

    # ==========================================
    # 3. SECURITY
    # ==========================================

    security_findings = analyze_security(file_path)

    print("\nSECURITY ANALYSIS")
    print("-" * 40)

    print(
        "Issues Detected:",
        len(security_findings)
    )

    if security_findings:

        for finding in security_findings:

            print("\nType:", finding["type"])
            print("Severity:", finding["severity"])
            print("Line:", finding["line"])
            print("Message:", finding["message"])
            print(
                "Recommendation:",
                finding["recommendation"]
            )

    else:

        print("No security issues detected.")

    # ==========================================
    # 4. BUG RISK
    # ==========================================

    bug_risk = predict_bug_risk(features)

    print("\nBUG RISK")
    print("-" * 40)

    print(
        "Risk Level:",
        bug_risk["risk_level"]
    )

    print(
        "Risk Probability:",
        bug_risk["risk_probability"],
        "%"
    )

    # ==========================================
    # 5. CODE DNA
    # ==========================================

    dna = generate_code_dna(features)

    print("\nCODE DNA")
    print("-" * 40)

    print(
        "Structural DNA:",
        dna["dna_string"]
    )

    print(
        "Fingerprint:",
        dna["fingerprint"]
    )

    # ==========================================
    # COMPLETE
    # ==========================================

    print("\n" + "=" * 60)
    print("              ANALYSIS COMPLETE")
    print("=" * 60)


# ==============================================
# COMMAND LINE INTERFACE
# ==============================================

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("\nUsage:")
        print("python analyze.py <python_file>")

        sys.exit(1)

    file_path = sys.argv[1]

    try:

        analyze_code(file_path)

    except FileNotFoundError:

        print("\nERROR: File not found.")

    except SyntaxError as error:

        print("\nERROR: Invalid Python syntax.")
        print("Line:", error.lineno)
        print("Message:", error.msg)