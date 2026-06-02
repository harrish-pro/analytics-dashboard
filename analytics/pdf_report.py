from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from analytics.data import (
    tasks_data,
    employee_performance
)

from analytics.summary import generate_summary


def create_pdf_report(file_path):

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    elements = []

    # TITLE

    title = Paragraph(
        "AI Productivity Analytics Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))


    # TASK DATA

    completed = tasks_data["Completed"]
    pending = tasks_data["Pending"]
    progress = tasks_data["In Progress"]

    task_text = f"""
    <b>Task Analytics</b><br/><br/>

    Completed Tasks: {completed}<br/>
    Pending Tasks: {pending}<br/>
    Tasks In Progress: {progress}
    """

    task_paragraph = Paragraph(
        task_text,
        styles['BodyText']
    )

    elements.append(task_paragraph)

    elements.append(Spacer(1, 20))


    # TOP EMPLOYEE

    top_employee = max(
        employee_performance,
        key=employee_performance.get
    )

    employee_text = f"""
    <b>Top Performing Employee</b><br/><br/>

    {top_employee} achieved the highest
    productivity score this week.
    """

    employee_paragraph = Paragraph(
        employee_text,
        styles['BodyText']
    )

    elements.append(employee_paragraph)

    elements.append(Spacer(1, 20))


    # EXECUTIVE SUMMARY

    summary = generate_summary()

    summary_paragraph = Paragraph(
        f"<b>Executive Summary</b><br/><br/>{summary}",
        styles['BodyText']
    )

    elements.append(summary_paragraph)

    doc.build(elements)