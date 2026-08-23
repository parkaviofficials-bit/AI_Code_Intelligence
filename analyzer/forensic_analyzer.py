def generate_forensic_report(similarity):

    if similarity >= 90:
        assessment = "VERY HIGH"
        explanation = "The two code samples have very similar structural characteristics."

    elif similarity >= 75:
        assessment = "HIGH"
        explanation = "The two code samples share many structural characteristics."

    elif similarity >= 50:
        assessment = "MODERATE"
        explanation = "The two code samples have some structural similarities."

    elif similarity >= 25:
        assessment = "LOW"
        explanation = "The two code samples have limited structural similarity."

    else:
        assessment = "VERY LOW"
        explanation = "The two code samples have substantially different structures."

    return {
        "similarity": similarity,
        "assessment": assessment,
        "explanation": explanation
    }