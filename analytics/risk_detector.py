def detect_dataset_risk(
    profile,
    health_score
):

    reasons = []

    risk_level = "Low"

    # Missing Values

    if profile["missing_values"] > 50:

        risk_level = "High"

        reasons.append(
            "Large number of missing values detected."
        )

    elif profile["missing_values"] > 10:

        risk_level = "Medium"

        reasons.append(
            "Moderate missing values detected."
        )

    # Duplicates

    if profile["duplicates"] > 20:

        risk_level = "High"

        reasons.append(
            "Large number of duplicate records detected."
        )

    elif profile["duplicates"] > 5:

        if risk_level != "High":

            risk_level = "Medium"

        reasons.append(
            "Duplicate records detected."
        )

    # Health Score

    if health_score < 60:

        risk_level = "High"

        reasons.append(
            "Poor dataset health score."
        )

    elif health_score < 80:

        if risk_level != "High":

            risk_level = "Medium"

        reasons.append(
            "Average dataset health score."
        )

    if len(reasons) == 0:

        reasons.append(
            "Dataset quality is excellent."
        )

    return {

        "risk_level": risk_level,

        "reasons": reasons

    }