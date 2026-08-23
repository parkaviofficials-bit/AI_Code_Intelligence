import ast


def calculate_complexity(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    tree = ast.parse(code)

    complexity = 1

    for node in ast.walk(tree):

        # Decision points
        if isinstance(node, ast.If):
            complexity += 1

        # Loops
        elif isinstance(node, (ast.For, ast.While)):
            complexity += 1

        # Exception handling
        elif isinstance(node, ast.ExceptHandler):
            complexity += 1

        # Boolean conditions
        elif isinstance(node, ast.BoolOp):
            complexity += len(node.values) - 1

    return complexity