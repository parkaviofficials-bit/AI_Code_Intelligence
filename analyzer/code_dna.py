import hashlib


def generate_code_dna(features):

    # Create a stable representation of the important
    # structural characteristics of the code.

    dna_string = (
        f"{features['functions']}-"
        f"{features['classes']}-"
        f"{features['if_statements']}-"
        f"{features['loops']}-"
        f"{features['returns']}-"
        f"{features['function_calls']}-"
        f"{features['imports']}-"
        f"{features['average_function_length']}-"
        f"{features['cyclomatic_complexity']}"
    )

    # Convert the structural representation into
    # a SHA-256 fingerprint.

    fingerprint = hashlib.sha256(
        dna_string.encode("utf-8")
    ).hexdigest()

    return {
        "dna_string": dna_string,
        "fingerprint": fingerprint
    }