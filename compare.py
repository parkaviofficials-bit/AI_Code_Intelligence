import sys

from analyzer.feature_extractor import extract_features
from analyzer.dna_similarity import calculate_similarity
from analyzer.forensic_analyzer import generate_forensic_report


def compare_code(file_a, file_b):

    print("\n" + "=" * 60)
    print("              CODE FORENSIC REPORT")
    print("=" * 60)

    print("\nFile A:", file_a)
    print("File B:", file_b)

    # Extract structural features
    features_a = extract_features(file_a)
    features_b = extract_features(file_b)

    # Calculate similarity
    similarity = calculate_similarity(
        features_a,
        features_b
    )

    # Interpret similarity
    report = generate_forensic_report(similarity)

    print("\nSTRUCTURAL SIMILARITY")
    print("-" * 40)

    print(
        "Similarity:",
        report["similarity"],
        "%"
    )

    print(
        "Assessment:",
        report["assessment"]
    )

    print("\nExplanation:")
    print(report["explanation"])

    print("\nFEATURE COMPARISON")
    print("-" * 40)

    feature_names = [
        "functions",
        "classes",
        "if_statements",
        "loops",
        "returns",
        "function_calls",
        "imports",
        "average_function_length",
        "cyclomatic_complexity"
    ]

    for feature in feature_names:

        value_a = features_a[feature]
        value_b = features_b[feature]

        print(
            f"{feature}: "
            f"{value_a} vs {value_b}"
        )

    print("\n" + "=" * 60)
    print("              COMPARISON COMPLETE")
    print("=" * 60)


if __name__ == "__main__":

    if len(sys.argv) != 3:

        print("\nUsage:")
        print(
            "python compare.py "
            "<file_a> <file_b>"
        )

        sys.exit(1)

    file_a = sys.argv[1]
    file_b = sys.argv[2]

    try:

        compare_code(file_a, file_b)

    except FileNotFoundError:

        print("\nERROR: One of the files was not found.")

    except SyntaxError as error:

        print("\nERROR: Invalid Python syntax.")
        print("Line:", error.lineno)
        print("Message:", error.msg)