import streamlit as st

st.set_page_config(
    page_title="HR Management System",
    page_icon="👨‍💼",
    layout="wide"
)
import pandas as pd
import matplotlib.pyplot as plt

from crud import view_all
from activity import get_recent_activity
from io import BytesIO

def dashboard():
    st.title("👨‍💼 Employee Dashboard")
    st.markdown("""
    
    <style>
    /* Main background */
    .stApp{
        background-color:#0E1117;
    }
    

    /* All headings and text */
    h1,h2,h3,h4,h5,h6,p,label,span{
        color:white !important;
    }

    /* Metric Cards */
    div[data-testid="stMetric"]{
        background:#1E1E2F;
        padding:15px;
        border-radius:15px;
        box-shadow:0px 4px 10px rgba(0,0,0,0.4);
    }

    /* Metric Labels */
    div[data-testid="stMetric"] label{
        color:#CFCFCF !important;
    }

    /* Metric Values */
    div[data-testid="stMetricValue"]{
        color:white !important;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"]{
        border-radius:15px;
        overflow:hidden;
    }

    </style>
    """, unsafe_allow_html=True)
    if st.button("🔄 Refresh Dashboard"):
        st.rerun()

    employees = view_all()

    columns = [
        "Employee ID",
        "Name",
        "Age",
        "Gender",
        "Department",
        "Designation",
        "Salary",
        "City",
        "Joining Date"
    ]

    df = pd.DataFrame(employees, columns=columns)

    if df.empty:
        st.warning("⚠️ No employee records found.")
        return
    df = df.sort_values("Employee ID")

    total = len(df)
    avg_salary = df["Salary"].mean()
    highest = df["Salary"].max()
    lowest = df["Salary"].min()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="👥 Total Employees",
            value=total
        )

    with c2:
        st.metric(
            label="💰 Average Salary",
            value=f"₹ {avg_salary:,.0f}"
        )

    with c3:
        st.metric(
            label="📈 Highest Salary",
            value=f"₹ {highest:,.0f}"
        )

    with c4:
        st.metric(
            label="📉 Lowest Salary",
            value=f"₹ {lowest:,.0f}"
        )

    st.divider()

    left, right = st.columns([2.5, 1.5])

    with left:
        st.subheader("🔍 Search & Filter")

        search_name = st.text_input("Search by Name")

        departments = ["All"] + sorted(df["Department"].unique().tolist())
        selected_department = st.selectbox(
            "Filter by Department",
            departments
        )

        filtered_df = df.copy()



        if search_name:
            filtered_df = filtered_df[
                filtered_df["Name"].str.contains(
                    search_name,
                    case=False,
                    na=False
                )
            ]

        if selected_department != "All":
            filtered_df = filtered_df[
                filtered_df["Department"] == selected_department
                ]
        excel_file = BytesIO()

        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            filtered_df.to_excel(writer, index=False, sheet_name="Employees")

        excel_file.seek(0)

        st.download_button(
            label="📥 Download Employee Data (Excel)",
            data=excel_file,
            file_name="Employee_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.subheader("📋 Employee Records")

        st.dataframe(
            filtered_df,
            width="stretch",
            hide_index=True,
            height=420
        )

    with right:
        st.subheader("📊 Department Statistics")

        department_count = df["Department"].value_counts()

        st.bar_chart(department_count)

        fig = department_count.plot.pie(
            autopct="%1.1f%%",
            ylabel=""
        ).get_figure()

        st.pyplot(fig)
        plt.close(fig)


        st.divider()

        st.subheader("💰 Average Salary by Department")

        salary_by_department = (
            df.groupby("Department")["Salary"]
            .mean()
            .sort_values(ascending=False)
        )

        st.bar_chart(salary_by_department)

        st.divider()

        st.subheader("🏆 Top 5 Highest Paid Employees")

        top5 = df.sort_values(
            by="Salary",
            ascending=False
        ).head(5)

        st.dataframe(
            top5[
                [
                    "Employee ID",
                    "Name",
                    "Department",
                    "Designation",
                    "Salary"
                ]
            ],
            hide_index=True,
            width="stretch"
        )

        st.divider()

        st.subheader("👨 Gender Distribution")

        gender_count = df["Gender"].value_counts()

        st.bar_chart(gender_count)

        fig = gender_count.plot.pie(
            autopct="%1.1f%%",
            ylabel=""
        ).get_figure()

        st.pyplot(fig)
        plt.close(fig)

        st.divider()

        st.subheader("🌍 City Distribution")

        city_count = df["City"].value_counts()

        st.bar_chart(city_count)

        fig = city_count.plot.pie(
            autopct="%1.1f%%",
            ylabel=""
        ).get_figure()

        st.pyplot(fig)
        plt.close(fig)

        st.divider()

        st.subheader("🕒 Recent Activity")

        activities = get_recent_activity()

        if activities:
            activity_df = pd.DataFrame(activities)

            activity_df = activity_df.rename(columns={
                "action": "Action",
                "emp_id": "Employee ID",
                "employee_name": "Employee Name",
                "action_time": "Time"
            })

            st.dataframe(
                activity_df.head(10),
                hide_index=True,
                width="stretch"
            )

        else:
            st.info("No recent activity found.")



