import streamlit as st
from crud import search_employee, delete_employee


def delete_page():

    st.title("🗑️ Delete Employee")

    emp_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    if st.button("🔍 Search"):

        employee = search_employee(emp_id)

        if employee:
            st.session_state["delete_employee"] = employee
        else:
            st.error("❌ Employee Not Found")

    if "delete_employee" in st.session_state:

        emp = st.session_state["delete_employee"]

        st.subheader("Employee Details")

        st.write(f"**ID:** {emp[0]}")
        st.write(f"**Name:** {emp[1]}")
        st.write(f"**Department:** {emp[4]}")
        st.write(f"**Designation:** {emp[5]}")
        st.write(f"**Salary:** ₹ {emp[6]:,.0f}")
        st.write(f"**City:** {emp[7]}")

        st.warning("⚠️ This action cannot be undone.")

        if st.button("🗑️ Delete Employee"):

            delete_employee(emp_id)

            st.success("✅ Employee Deleted Successfully!")

            del st.session_state["delete_employee"]