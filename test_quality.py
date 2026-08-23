from analyzer.feature_extractor import extract_features
from analyzer.quality_analyzer import calculate_quality_score


file_path = "test_code/sample.py"

features = extract_features(file_path)

quality = calculate_quality_score(features)

print("\nCODE QUALITY REPORT")
print("----------------------------")
print("Quality Score:", quality["score"], "/ 100")
print("Category:", quality["category"])

if quality["reasons"]:
    print("\nIssues:")
    for reason in quality["reasons"]:
        print("-", reason)
else:
    print("\nNo major quality issues detected.")