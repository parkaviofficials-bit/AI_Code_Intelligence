import ast

code = """
def student_result(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"
"""

tree = ast.parse(code)

print(ast.dump(tree, indent=4))