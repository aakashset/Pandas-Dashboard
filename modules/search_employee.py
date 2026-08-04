import streamlit as st
from crud import search_employee


def search_page():

    st.title("🔍 Search Employee")

    emp_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        employee = search_employee(emp_id)

        if employee:

            st.success("Employee Found ✅")

            c1, c2 = st.columns(2)

            with c1:
                st.write("### Personal Details")
                st.write(f"**Employee ID:** {employee[0]}")
                st.write(f"**Name:** {employee[1]}")
                st.write(f"**Age:** {employee[2]}")
                st.write(f"**Gender:** {employee[3]}")
                st.write(f"**City:** {employee[7]}")

            with c2:
                st.write("### Work Details")
                st.write(f"**Department:** {employee[4]}")
                st.write(f"**Designation:** {employee[5]}")
                st.write(f"**Salary:** ₹ {employee[6]:,.0f}")
                st.write(f"**Joining Date:** {employee[8]}")

        else:
            st.error("Employee Not Found ❌")