def generate_scorecard(
    health_score,
    risk_report
):

    # Grade

    if health_score >= 90:
        grade = "A"

    elif health_score >= 80:
        grade = "B"

    elif health_score >= 70:
        grade = "C"

    elif health_score >= 60:
        grade = "D"

    else:
        grade = "F"

    # Confidence

    if risk_report["risk_level"] == "Low":

        confidence = "High"

    elif risk_report["risk_level"] == "Medium":

        confidence = "Medium"

    else:

        confidence = "Low"

    # Overall Status

    if grade in ["A", "B"]:

        status = "Ready for Business Use"

    elif grade == "C":

        status = "Needs Review"

    else:

        status = "Requires Attention"

    return {

        "grade": grade,

        "confidence": confidence,

        "status": status

    }