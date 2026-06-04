from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(report_data, file_path):

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    elements = []

    profile = report_data["profile"]
    statistics = report_data["statistics"]
    summary = report_data["summary"]

    # TITLE

    elements.append(
        Paragraph(
            "AI ANALYTICS REPORT",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # EXECUTIVE SUMMARY

    elements.append(
        Paragraph(
            "1. Executive Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # DATASET OVERVIEW

    elements.append(
        Paragraph(
            "2. Dataset Overview",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"""
            Total Rows: {profile['rows']}<br/>
            Total Columns: {profile['columns']}<br/>
            Missing Values: {profile['missing_values']}<br/>
            Duplicate Records: {profile['duplicates']}
            """,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # COLUMN ANALYSIS

    elements.append(
        Paragraph(
            "3. Column Analysis",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"Columns: {', '.join(profile['column_names'])}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Numeric Columns: {', '.join(profile['numeric_columns'])}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Text Columns: {', '.join(profile['text_columns'])}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # STATISTICS

    elements.append(
        Paragraph(
            "4. Statistical Analysis",
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

        elements.append(Spacer(1, 10))

    # DATA QUALITY

    elements.append(
        Paragraph(
            "5. Data Quality Assessment",
            styles["Heading1"]
        )
    )

    quality_text = f"""
    Missing Values Found: {profile['missing_values']}<br/>
    Duplicate Records Found: {profile['duplicates']}
    """

    elements.append(
        Paragraph(
            quality_text,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # VISUAL ANALYTICS

    if "chart_image" in report_data:

        elements.append(
            Paragraph(
                "6. Visual Analytics",
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

        elements.append(Spacer(1, 20))

    # RECOMMENDATIONS

    elements.append(
        Paragraph(
            "7. Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = """
    • Review missing values before making decisions.<br/>
    • Validate duplicate records regularly.<br/>
    • Focus on high-performing metrics identified in analysis.<br/>
    • Monitor trends using generated dashboards.<br/>
    """

    elements.append(
        Paragraph(
            recommendations,
            styles["BodyText"]
        )
    )

    doc.build(elements)