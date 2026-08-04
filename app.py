import streamlit as st

st.set_page_config(
    page_title="Employee Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)

from modules.dashboard import dashboard
from modules.add_employee import add_page
from modules.update_employee import update_page
from modules.delete_employee import delete_page
from modules.search_employee import search_page
from login import login

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()



st.sidebar.title("👨‍💼 Employee Management")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Employee",
        "Update Employee",
        "Delete Employee",
        "Search Employee"
    ]
)

if page == "Dashboard":
    dashboard()

elif page == "Add Employee":
    add_page()

elif page == "Update Employee":
    update_page()

elif page == "Delete Employee":
    delete_page()

elif page == "Search Employee":
    search_page()

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()