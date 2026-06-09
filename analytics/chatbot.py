def answer_question(
    question,
    profile,
    health_score,
    risk_report,
    scorecard
):

    question = question.lower()

    # ROWS

    if "row" in question:

        return (
            f"The dataset contains "
            f"{profile['rows']} rows."
        )

    # COLUMNS

    elif "column" in question:

        return (
            f"The dataset contains "
            f"{profile['columns']} columns."
        )

    # HEALTH

    elif "health" in question:

        return (
            f"The dataset health score "
            f"is {health_score}%."
        )

    # RISK

    elif "risk" in question:

        return (
            f"The risk level is "
            f"{risk_report['risk_level']}."
        )

    # GRADE

    elif "grade" in question:

        return (
            f"The dataset grade "
            f"is {scorecard['grade']}."
        )

    # STATUS

    elif "status" in question:

        return (
            scorecard["status"]
        )

    # DEFAULT

    return (
        "I cannot answer that question yet."
    )