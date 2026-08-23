from analyzer.feature_extractor import extract_features
from analyzer.security_analyzer import analyze_security
from analyzer.bug_predictor import predict_bug_risk
from analyzer.recommendation_engine import generate_recommendations


file_path = "test_code/sample.py"

features = extract_features(file_path)

security_issues = analyze_security(file_path)

bug_risk = predict_bug_risk(features)

recommendations = generate_recommendations(
    features,
    security_issues,
    bug_risk
)

print("\nRECOMMENDATION REPORT")
print("----------------------------")

for item in recommendations:

    print("\nType:", item["type"])
    print("Severity:", item["severity"])
    print("Message:", item["message"])
    print("Recommendation:", item["recommendation"])