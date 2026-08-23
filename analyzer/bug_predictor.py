import pandas as pd

from sklearn.ensemble import RandomForestClassifier


def train_bug_model():

    # ---------------------------------------------------------
    # Demonstration training data
    # ---------------------------------------------------------
    # 0 = lower demonstrated bug risk
    # 1 = higher demonstrated bug risk
    #
    # This is a prototype dataset created for the project.
    # A research-grade system should eventually use labelled
    # real-world repositories and verified bug histories.

    data = {
        "lines_of_code": [
            8, 10, 12, 15, 18, 20, 25, 30, 35, 40,
            45, 50, 55, 60, 70, 80, 90, 100, 120, 150,
            10, 15, 20, 25, 30, 40, 50, 65, 80, 100
        ],

        "functions": [
            1, 1, 1, 2, 2, 2, 3, 3, 4, 4,
            4, 5, 5, 6, 7, 8, 9, 10, 12, 15,
            1, 2, 2, 3, 3, 4, 5, 6, 8, 10
        ],

        "if_statements": [
            0, 0, 1, 1, 1, 1, 2, 2, 3, 3,
            4, 5, 5, 6, 7, 8, 10, 12, 15, 20,
            0, 1, 1, 2, 2, 3, 5, 7, 10, 14
        ],

        "loops": [
            0, 0, 0, 0, 1, 1, 1, 1, 1, 2,
            2, 2, 3, 3, 4, 4, 5, 6, 7, 10,
            0, 0, 1, 1, 1, 2, 2, 3, 4, 6
        ],

        "returns": [
            1, 1, 1, 2, 2, 2, 3, 3, 4, 4,
            5, 5, 6, 7, 8, 9, 10, 12, 15, 18,
            1, 2, 2, 3, 3, 4, 5, 6, 8, 10
        ],

        "function_calls": [
            1, 1, 2, 2, 2, 3, 3, 4, 4, 5,
            6, 7, 8, 9, 10, 12, 14, 16, 20, 25,
            1, 2, 2, 3, 4, 5, 7, 9, 12, 16
        ],

        "imports": [
            0, 0, 1, 1, 1, 1, 1, 2, 2, 2,
            3, 3, 3, 4, 4, 4, 5, 5, 6, 7,
            0, 1, 1, 1, 2, 2, 3, 4, 5, 6
        ],

        "average_function_length": [
            3, 4, 4, 5, 5, 6, 6, 7, 8, 8,
            10, 12, 14, 15, 17, 18, 20, 23, 27, 32,
            4, 5, 6, 7, 8, 10, 12, 15, 20, 25
        ],

        "cyclomatic_complexity": [
            1, 1, 1, 2, 2, 2, 3, 3, 3, 4,
            4, 5, 5, 6, 7, 8, 10, 12, 15, 20,
            1, 2, 2, 3, 4, 5, 6, 8, 10, 13
        ],

        "bug_risk": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1
        ]
    }

    df = pd.DataFrame(data)

    X = df.drop("bug_risk", axis=1)
    y = df["bug_risk"]

    model = RandomForestClassifier(
        n_estimators=200,
        min_samples_leaf=2,
        random_state=42
    )

    model.fit(X, y)

    return model


def predict_bug_risk(features):

    model = train_bug_model()

    feature_names = [
        "lines_of_code",
        "functions",
        "if_statements",
        "loops",
        "returns",
        "function_calls",
        "imports",
        "average_function_length",
        "cyclomatic_complexity"
    ]

    input_data = pd.DataFrame(
        [[features[name] for name in feature_names]],
        columns=feature_names
    )

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    risk_probability = probabilities[1] * 100

    # Interpret the predicted probability
    if risk_probability >= 70:
        risk_level = "HIGH"

    elif risk_probability >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    # ---------------------------------------------------------
    # MODEL EXPLAINABILITY
    # ---------------------------------------------------------
    # Random Forest provides feature importance values.
    # These values indicate which structural features contributed
    # most to the model's overall decision process.
    #
    # Important:
    # Feature importance is NOT proof that a specific feature
    # caused a bug. It only describes the model's learned
    # importance within this demonstration dataset.

    importance_pairs = list(
        zip(
            feature_names,
            model.feature_importances_
        )
    )

    importance_pairs.sort(
        key=lambda item: item[1],
        reverse=True
    )

    top_features = [
        {
            "feature": feature,
            "importance": round(float(importance), 4)
        }
        for feature, importance in importance_pairs[:3]
    ]

    return {
        "prediction": int(prediction),
        "risk_probability": round(risk_probability, 2),
        "risk_level": risk_level,
        "top_features": top_features
    }