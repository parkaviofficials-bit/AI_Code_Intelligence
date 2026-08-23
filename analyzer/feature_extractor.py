import ast


def extract_features(file_path):

    # Read source code
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    # Parse source code into AST
    tree = ast.parse(code)

    # Count non-empty lines
    lines = [
        line for line in code.splitlines()
        if line.strip()
    ]

    function_lengths = []

    features = {
        "lines_of_code": len(lines),
        "functions": 0,
        "classes": 0,
        "if_statements": 0,
        "loops": 0,
        "returns": 0,
        "function_calls": 0,
        "imports": 0,
        "average_function_length": 0,
        "cyclomatic_complexity": 1,
    }

    for node in ast.walk(tree):

        # Functions
        if isinstance(node, ast.FunctionDef):
            features["functions"] += 1

            if node.lineno and node.end_lineno:
                length = node.end_lineno - node.lineno + 1
                function_lengths.append(length)

        # Classes
        elif isinstance(node, ast.ClassDef):
            features["classes"] += 1

        # If statements
        elif isinstance(node, ast.If):
            features["if_statements"] += 1
            features["cyclomatic_complexity"] += 1

        # Loops
        elif isinstance(node, (ast.For, ast.While)):
            features["loops"] += 1
            features["cyclomatic_complexity"] += 1

        # Exception handlers
        elif isinstance(node, ast.ExceptHandler):
            features["cyclomatic_complexity"] += 1

        # Boolean conditions
        elif isinstance(node, ast.BoolOp):
            features["cyclomatic_complexity"] += len(node.values) - 1

        # Returns
        elif isinstance(node, ast.Return):
            features["returns"] += 1

        # Function calls
        elif isinstance(node, ast.Call):
            features["function_calls"] += 1

        # Imports
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            features["imports"] += 1

    # Average function length
    if function_lengths:
        features["average_function_length"] = round(
            sum(function_lengths) / len(function_lengths),
            2
        )

    return features