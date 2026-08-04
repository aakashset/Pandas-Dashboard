import streamlit as st
from crud import search_employee, update_employee


def update_page():

    st.title("✏️ Update Employee")

    emp_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    if st.button("🔍 Search"):

        employee = search_employee(emp_id)

        if employee:
            st.session_state["employee"] = employee
        else:
            st.error("❌ Employee Not Found")

    if "employee" in st.session_state:

        emp = st.session_state["employee"]

        name = st.text_input("Name", value=emp[1])

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=65,
            value=int(emp[2])
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"],
            index=0 if emp[3].lower() == "male" else 1
        )

        department = st.text_input(
            "Department",
            value=emp[4]
        )

        designation = st.text_input(
            "Designation",
            value=emp[5]
        )

        salary = st.number_input(
            "Salary",
            min_value=0.0,
            value=float(emp[6])
        )

        city = st.text_input(
            "City",
            value=emp[7]
        )

        joining_date = st.date_input(
            "Joining Date",
            value=emp[8]
        )

        if st.button("✅ Update Employee"):

            update_employee(
                emp_id,
                name,
                age,
                gender,
                department,
                designation,
                salary,
                city,
                joining_date
            )

            st.success("✅ Employee Updated Successfully!")