from analyzer.complexity_analyzer import calculate_complexity


file_path = "test_code/sample.py"

complexity = calculate_complexity(file_path)

print("CODE COMPLEXITY")
print("--------------------")
print("Cyclomatic Complexity:", complexity)