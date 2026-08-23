from analyzer.security_analyzer import analyze_security


file_path = "test_code/security_sample.py"

findings = analyze_security(file_path)

print("\nSECURITY REPORT")
print("----------------------------")

if not findings:
    print("No security issues detected.")

else:
    print("Issues detected:", len(findings))

    for finding in findings:
        print("\nType:", finding["type"])
        print("Severity:", finding["severity"])
        print("Line:", finding["line"])
        print("Message:", finding["message"])
        print("Recommendation:", finding["recommendation"])