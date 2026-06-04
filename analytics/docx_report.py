from docx import Document


def create_docx_report(
    report_data,
    file_path
):

    doc = Document()

    doc.add_heading(
        "AI Analytics Report",
        level=1
    )

    profile = report_data["profile"]

    doc.add_paragraph(
        f"""
Rows: {profile['rows']}
Columns: {profile['columns']}
Missing Values: {profile['missing_values']}
Duplicates: {profile['duplicates']}
"""
    )

    doc.add_heading(
        "Executive Summary",
        level=2
    )

    doc.add_paragraph(
        report_data["summary"]
    )

    doc.save(file_path)