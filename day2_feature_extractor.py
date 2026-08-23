import ast

code = """
def student_result(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"
"""

tree = ast.parse(code)

features = {
    "functions": 0,
    "if_statements": 0,
    "loops": 0,
    "returns": 0,
}

for node in ast.walk(tree):

    if isinstance(node, ast.FunctionDef):
        features["functions"] += 1

    elif isinstance(node, ast.If):
        features["if_statements"] += 1

    elif isinstance(node, (ast.For, ast.While)):
        features["loops"] += 1

    elif isinstance(node, ast.Return):
        features["returns"] += 1

print(features)