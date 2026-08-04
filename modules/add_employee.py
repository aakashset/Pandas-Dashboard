import streamlit as st
from crud import add_employee


def add_page():

    st.title("➕ Add Employee")

    emp_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Employee Name")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    department = st.selectbox(
        "Department",
        [
            "IT",
            "HR",
            "Finance",
            "Marketing",
            "Sales"
        ]
    )

    designation = st.text_input("Designation")

    salary = st.number_input(
        "Salary",
        min_value=1000
    )

    city = st.text_input("City")

    joining_date = st.date_input(
        "Joining Date"
    )

    if st.button("Add Employee"):

        add_employee(
            emp_id,
            name,
            age,
            gender,
            department,
            designation,
            salary,
            city,
            str(joining_date)
        )

        st.success("Employee Added Successfully!")