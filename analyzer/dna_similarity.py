import math


def normalize(value, maximum):
    if maximum == 0:
        return 0
    return value / maximum


def calculate_similarity(features_a, features_b):

    feature_limits = {
        "functions": 20,
        "classes": 10,
        "if_statements": 20,
        "loops": 20,
        "returns": 20,
        "function_calls": 30,
        "imports": 20,
        "average_function_length": 50,
        "cyclomatic_complexity": 20
    }

    feature_names = list(feature_limits.keys())

    vector_a = []
    vector_b = []

    for name in feature_names:

        limit = feature_limits[name]

        value_a = normalize(
            features_a[name],
            limit
        )

        value_b = normalize(
            features_b[name],
            limit
        )

        vector_a.append(value_a)
        vector_b.append(value_b)

    # Calculate normalized Euclidean distance
    distance = math.sqrt(
        sum(
            (a - b) ** 2
            for a, b in zip(vector_a, vector_b)
        )
    )

    # Maximum possible distance for our normalized vectors
    max_distance = math.sqrt(len(feature_names))

    similarity = (
        1 - (distance / max_distance)
    ) * 100

    similarity = max(0, min(100, similarity))

    return round(similarity, 2)