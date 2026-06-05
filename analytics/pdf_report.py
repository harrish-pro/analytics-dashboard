from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_pdf_report(
    report_data,
    file_path
):

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    elements = []

    profile = report_data["profile"]
    statistics = report_data["statistics"]
    summary = report_data["summary"]

    health_score = report_data["health_score"]

    insights = report_data["insights"]

    recommendations = report_data["recommendations"]

    # TITLE

    elements.append(
        Paragraph(
            "AI Analytics Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # EXECUTIVE SUMMARY

    elements.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # HEALTH SCORE

    elements.append(
        Paragraph(
            "Dataset Health Score",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"{health_score}%",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # DATASET OVERVIEW

    elements.append(
        Paragraph(
            "Dataset Overview",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"""
            Rows: {profile['rows']}<br/>
            Columns: {profile['columns']}<br/>
            Missing Values: {profile['missing_values']}<br/>
            Duplicates: {profile['duplicates']}
            """,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # STATISTICS

    elements.append(
        Paragraph(
            "Statistical Analysis",
            styles["Heading1"]
        )
    )

    for column, values in statistics.items():

        elements.append(
            Paragraph(
                f"""
                <b>{column}</b><br/>
                Average: {values['mean']}<br/>
                Maximum: {values['max']}<br/>
                Minimum: {values['min']}<br/>
                Total: {values['sum']}
                """,
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

    elements.append(
        Spacer(1, 20)
    )

    # AI INSIGHTS

    elements.append(
        Paragraph(
            "AI Business Insights",
            styles["Heading1"]
        )
    )

    for insight in insights:

        elements.append(
            Paragraph(
                f"• {insight}",
                styles["BodyText"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    # RECOMMENDATIONS

    elements.append(
        Paragraph(
            "Recommendations",
            styles["Heading1"]
        )
    )

    for recommendation in recommendations:

        elements.append(
            Paragraph(
                f"• {recommendation}",
                styles["BodyText"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    # CHART IMAGE (OPTIONAL)

    if report_data.get("chart_image"):

        try:

            elements.append(
                Paragraph(
                    "Visual Analytics",
                    styles["Heading1"]
                )
            )

            elements.append(
                Image(
                    report_data["chart_image"],
                    width=450,
                    height=250
                )
            )

            elements.append(
                Spacer(1, 20)
            )

        except Exception:
            pass

    doc.build(elements)