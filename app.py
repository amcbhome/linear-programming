import streamlit as st
import pandas as pd
from pulp import *
# Removed: import matplotlib.pyplot as plt
# Removed: import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="LP for Scheduling Problems",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Title and Introduction ---
st.title("Optimizing Scheduling with Linear Programming")
st.markdown("---")
st.write(
    "This application demonstrates how Linear Programming (LP) can be used to solve "
    "simplified scheduling problems. LP helps in making optimal decisions when "
    "faced with limited resources and specific objectives."
)

# --- What is a Scheduling Problem with LP? ---
st.header("What is a Scheduling Problem Solved with Linear Programming?")
st.markdown(
    """
    Scheduling problems involve allocating resources (e.g., time, personnel, machines) to tasks over a period to achieve an optimal outcome. When solved with Linear Programming, these problems are formulated mathematically, consisting of:

    * **Decision Variables**: Represent the choices (e.g., how many people to assign to a shift).
    * **Objective Function**: The goal to optimize (e.g., minimize cost, maximize profit).
    * **Constraints**: Limitations or rules that must be followed (e.g., minimum staff required, maximum working hours).

    By defining these components as linear expressions, LP solvers can find the best possible solution.
    """
)
st.markdown("---")

# --- Example Exercise: Workforce Scheduling ---
st.header("Example: Simplified Workforce Scheduling")
st.write(
    "Imagine a small café that needs to schedule its staff for a day. "
    "They have different staffing requirements for different time slots."
)

st.subheader("Requirements:")
st.markdown(
    """
    * **Morning (8 AM - 12 PM):** At least 2 staff
    * **Afternoon (12 PM - 4 PM)::** At least 3 staff
    * **Evening (4 PM - 8 PM):** At least 2 staff
    """
)

st.subheader("Employee Shifts:")
st.markdown(
    """
    * **Shift 1 (S1):** 8 AM - 4 PM (8 hours)
    * **Shift 2 (S2):** 12 PM - 8 PM (8 hours)
    """
)

st.write("Each employee works one 8-hour shift. We want to minimize the total number of employees needed.")

st.subheader("Conceptual LP Formulation:")
st.markdown(
    """
    Let:
    * `$x_1$` = Number of employees on Shift 1
    * `$x_2$` = Number of employees on Shift 2

    **Objective Function (Minimize Total Employees):**
    `Min Z = x1 + x2`

    **Constraints:**
    * **Morning (8 AM - 12 PM):** Employees on S1 cover this.
        `$x_1 \ge 2$`
    * **Afternoon (12 PM - 4 PM):** Employees on S1 and S2 cover this.
        `$x_1 + x_2 \ge 3$`
    * **Evening (4 PM - 8 PM):** Employees on S2 cover this.
        `$x_2 \ge 2$`
    * **Non-negativity:**
        `$x_1 \ge 0, x_2 \ge 0$`
        (Also, `$x_1$` and `$x_2$` should ideally be integers for real-world application, making it an Integer Linear Programming problem.)
    """
)

# --- Solve the problem (conceptual/illustrative) ---
st.subheader("Illustrative Solution:")

# Create the problem variable
prob = LpProblem("Cafe_Staffing", LpMinimize)

# Decision Variables
x1 = LpVariable("Shift1_Employees", 0, None, LpInteger)
x2 = LpVariable("Shift2_Employees", 0, None, LpInteger)

# Objective Function
prob += x1 + x2, "Total_Employees"

# Constraints
prob += x1 >= 2, "Morning_Coverage"
prob += x1 + x2 >= 3, "Afternoon_Coverage"
prob += x2 >= 2, "Evening_Coverage"

# Solve the problem
prob.solve()

optimal_x1 = None
optimal_x2 = None
optimal_obj_val = None

if LpStatus[prob.status] == "Optimal":
    st.success(f"**Optimal Solution Found!** (Status: {LpStatus[prob.status]})")
    optimal_x1 = x1.varValue
    optimal_x2 = x2.varValue
    optimal_obj_val = value(prob.objective)
    st.write(f"Number of employees for Shift 1: **{int(optimal_x1)}**")
    st.write(f"Number of employees for Shift 2: **{int(optimal_x2)}**")
    st.write(f"**Minimum Total Employees Needed: {int(optimal_obj_val)}**")
else:
    st.warning(f"No optimal solution found. Status: {LpStatus[prob.status]}")

st.write(
    "*(This is a simplified example. Real-world scheduling problems involve many more variables and constraints.)*"
)
st.markdown("---")

# Removed: Feasible Region Graph Section
# All code related to matplotlib plotting was removed from here.

# --- Top 10 Uses Section ---
st.header("Top 10 Uses of Linear Programming in Scheduling")
st.markdown(
    """
    Here are key areas where Linear Programming is applied to optimize scheduling:

    1.  **Staff/Workforce Scheduling**: Minimizing labor costs while meeting demand and adhering to labor laws, employee preferences, and skill requirements (e.g., nurse scheduling in hospitals, call center staffing, bus driver rosters).
    2.  **Production Planning and Scheduling**: Optimizing production runs to meet demand, minimize inventory costs, and efficiently utilize machinery and raw materials.
    3.  **Transportation and Logistics Scheduling**: Determining optimal routes and schedules for fleets of vehicles (e.g., delivery trucks, airlines) to minimize fuel consumption, travel time, or maximize deliveries.
    4.  **Resource Allocation**: Distributing limited resources (e.g., budget, equipment, raw materials) among competing projects or tasks to achieve specific objectives.
    5.  **Project Scheduling**: Optimizing the timeline and resource allocation for complex projects to meet deadlines and minimize costs.
    6.  **Energy Management Scheduling**: Planning the operation of power plants or energy consumption in industrial facilities to minimize costs or carbon emissions.
    7.  **Machine Scheduling**: Optimizing the sequence of jobs on machines to minimize completion time, maximize throughput, or reduce setup costs.
    8.  **Classroom/University Timetabling**: Creating optimal class schedules that accommodate student and instructor preferences, room availability, and minimize conflicts.
    9.  **Maintenance Scheduling**: Planning maintenance activities for equipment or infrastructure to minimize downtime and extend asset life.
    10. **Event Scheduling**: Optimizing the timing and resource allocation for large-scale events, conferences, or sports tournaments to manage venues, staff, and participant flow.
    """
)
st.markdown("---")
