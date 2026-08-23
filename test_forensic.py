from analyzer.feature_extractor import extract_features
from analyzer.dna_similarity import calculate_similarity
from analyzer.forensic_analyzer import generate_forensic_report


file_a = "test_code/sample.py"
file_b = "test_code/sample2.py"

features_a = extract_features(file_a)
features_b = extract_features(file_b)

similarity = calculate_similarity(
    features_a,
    features_b
)

report = generate_forensic_report(similarity)

print("\nCODE FORENSIC REPORT")
print("=" * 40)

print("File A:", file_a)
print("File B:", file_b)

print("\nStructural Similarity:",
      report["similarity"], "%")

print("Assessment:",
      report["assessment"])

print("\nExplanation:")
print(report["explanation"])