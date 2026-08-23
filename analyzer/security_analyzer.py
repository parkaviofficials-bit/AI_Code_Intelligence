import ast


def analyze_security(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    tree = ast.parse(code)

    findings = []

    for node in ast.walk(tree):

        # Dangerous eval()
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id == "eval":
                    findings.append({
                        "type": "Dangerous Function",
                        "severity": "HIGH",
                        "line": node.lineno,
                        "message": "eval() can execute dynamically generated code.",
                        "recommendation": "Avoid eval() and use safer parsing methods."
                    })

                # Dangerous exec()
                elif node.func.id == "exec":
                    findings.append({
                        "type": "Dangerous Function",
                        "severity": "HIGH",
                        "line": node.lineno,
                        "message": "exec() can execute dynamically generated code.",
                        "recommendation": "Avoid exec() unless absolutely necessary."
                    })

        # os.system()
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if (
                    isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "os"
                    and node.func.attr == "system"
                ):
                    findings.append({
                        "type": "Command Execution",
                        "severity": "HIGH",
                        "line": node.lineno,
                        "message": "os.system() executes operating-system commands.",
                        "recommendation": "Use safer subprocess APIs with controlled arguments."
                    })

        # Hard-coded sensitive variables
        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):

                    name = target.id.lower()

                    sensitive_words = [
                        "password",
                        "passwd",
                        "secret",
                        "api_key",
                        "apikey",
                        "token"
                    ]

                    if any(word in name for word in sensitive_words):

                        if isinstance(node.value, ast.Constant):
                            if isinstance(node.value.value, str):

                                findings.append({
                                    "type": "Hard-coded Secret",
                                    "severity": "HIGH",
                                    "line": node.lineno,
                                    "message": "A possible secret is hard-coded in source code.",
                                    "recommendation": "Use environment variables or a secure secret manager."
                                })

    return findings