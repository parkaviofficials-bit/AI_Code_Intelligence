import ast

code = """
def student_result(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"
"""

tree = ast.parse(code)

functions = 0
if_statements = 0
returns = 0
loops = 0

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        functions += 1

    elif isinstance(node, ast.If):
        if_statements += 1

    elif isinstance(node, ast.Return):
        returns += 1

    elif isinstance(node, (ast.For, ast.While)):
        loops += 1

print("Functions:", functions)
print("If statements:", if_statements)
print("Return statements:", returns)
print("Loops:", loops)