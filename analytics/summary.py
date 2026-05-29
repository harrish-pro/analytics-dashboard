from analytics.data import (
    tasks_data,
    employee_performance
)

def generate_summary():

    completed = tasks_data["Completed"]
    pending = tasks_data["Pending"]

    top_employee = max(
        employee_performance,
        key=employee_performance.get
    )

    summary = f"""
    This week's productivity analytics show strong
    task completion performance across the company.

    Total completed tasks reached {completed},
    while only {pending} tasks remain pending.

    Employee performance metrics indicate that
    {top_employee} achieved the highest productivity score.

    Overall workflow efficiency remains stable
    with positive team engagement.
    """

    return summary