from docx import Document

from analytics.data import (
    tasks_data,
    employee_performance
)

from analytics.summary import generate_summary


def create_docx_report(file_path):

    doc = Document()

    # TITLE

    doc.add_heading(
        'AI Productivity Analytics Report',
        level=1
    )


    # TASK SECTION

    doc.add_heading(
        'Task Analytics',
        level=2
    )

    doc.add_paragraph(
        f"""
        Completed Tasks: {tasks_data["Completed"]}

        Pending Tasks: {tasks_data["Pending"]}

        Tasks In Progress: {tasks_data["In Progress"]}
        """
    )


    # EMPLOYEE SECTION

    top_employee = max(
        employee_performance,
        key=employee_performance.get
    )

    doc.add_heading(
        'Top Employee',
        level=2
    )

    doc.add_paragraph(
        f"{top_employee} achieved the highest productivity score."
    )


    # EXECUTIVE SUMMARY

    doc.add_heading(
        'Executive Summary',
        level=2
    )

    doc.add_paragraph(
        generate_summary()
    )


    doc.save(file_path)