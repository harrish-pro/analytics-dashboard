import plotly.express as px

from analytics.data import (
    tasks_data,
    weekly_productivity,
    employee_performance
)


# PIE CHART

def create_task_chart():

    fig = px.pie(
        names=list(tasks_data.keys()),
        values=list(tasks_data.values()),
        title="Task Status Overview",
        hole=0.4
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white")
    )

    return fig.to_html(full_html=False)


# LINE CHART

def create_productivity_chart():

    fig = px.line(
        x=list(weekly_productivity.keys()),
        y=list(weekly_productivity.values()),
        title="Weekly Productivity",
        markers=True
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white")
    )

    return fig.to_html(full_html=False)


# BAR CHART

def create_employee_chart():

    fig = px.bar(
        x=list(employee_performance.keys()),
        y=list(employee_performance.values()),
        title="Employee Performance",
        text_auto=True
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white")
    )

    return fig.to_html(full_html=False)