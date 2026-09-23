# 👨‍💼 Employee Management Dashboard

A Python-based **Employee Management Dashboard** built using **Streamlit**, with employee data handling, CRUD operations, search functionality, and an interactive dashboard.

The project demonstrates how Python can be used to build an interactive data-management application with a simple web interface.

---

## 📌 Project Overview

This project provides an interactive interface for managing employee records.

The application allows users to:

* 🔐 Login to the application
* 📊 View an employee dashboard
* ➕ Add employees
* ✏️ Update employee information
* 🗑️ Delete employees
* 🔎 Search employees
* 🚪 Logout securely from the application

The main Streamlit application uses separate modules for the dashboard, employee creation, updating, deletion, and searching.

---

# 🔄 End-to-End Project Flow

```text
                         👤 User
                           │
                           ▼
                    🔐 Login Page
                           │
                           ▼
                  🖥️ Streamlit App
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        📊 Dashboard    ➕ Add       ✏️ Update
                           │             │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        🗑️ Delete      🔎 Search     📋 View
                           │
                           ▼
                   Employee Data
                           │
                           ▼
                    CRUD Operations
                           │
                           ▼
                    Data Storage
```

### How it works

1. The user launches the Streamlit application.
2. The login screen authenticates the user.
3. After login, the Employee Management sidebar becomes available.
4. The user can navigate between Dashboard, Add Employee, Update Employee, Delete Employee, and Search Employee.
5. CRUD functions perform the required employee data operations.
6. The updated employee information is displayed through the Streamlit interface.

The main application controls login state using Streamlit session state and provides sidebar navigation for the employee-management operations.

---

# ✨ Features

## 🔐 Login

The application includes a login interface before users can access the employee-management dashboard.

The login state is maintained using Streamlit session state.

---

## 📊 Dashboard

The dashboard provides an interactive view of employee-related information.

The dashboard is implemented as a separate module and loaded through the main Streamlit application.

---

## ➕ Add Employee

Users can add new employee records by providing information such as:

* Employee ID
* Name
* Age
* Gender
* Department
* Designation
* Salary
* City
* Joining Date

The employee information is passed to the CRUD layer for processing.

---

## ✏️ Update Employee

The application provides functionality to update employee information.

The current management interface includes salary-update functionality through the CRUD layer.

---

## 🗑️ Delete Employee

Users can delete an employee record by providing the employee ID.

---

## 🔎 Search Employee

Users can search for an employee using the employee ID.

When an employee is found, the application displays details including:

* Employee ID
* Name
* Age
* Gender
* Department
* Designation
* Salary
* City
* Joining Date

---

# 🛠️ Tech Stack

| Technology    | Purpose                                    |
| ------------- | ------------------------------------------ |
| 🐍 Python     | Core Programming Language                  |
| 🖥️ Streamlit | Interactive Web Application                |
| 🐼 Pandas     | Data Analysis and Data Handling            |
| 🗄️ MySQL     | Database / Data Storage                    |
| 🔄 CRUD       | Create, Read, Update and Delete Operations |

---

# 🏗️ Project Structure

```text
Pandas-Dashboard/
│
├── modules/
│   ├── dashboard.py
│   ├── add_employee.py
│   ├── update_employee.py
│   ├── delete_employee.py
│   └── search_employee.py
│
├── app.py
├── login.py
├── crud.py
├── database.py
├── ui.py
├── activity.py
├── bonus.py
├── functions.py
├── functions for matching records.py
│
├── csv_demo.py
├── new csv.py
├── new pr.py
│
├── employees.csv
├── emp.csv
├── employee_master_25.csv
├── employee_updates_25.csv
│
├── customers.csv
├── customer_bonus.csv
│
├── TopRichestInWorld.csv
├── TopRichestInWorld(1).csv
│
└── requirements.txt
```

The repository contains a dedicated `modules` directory for the Streamlit employee-management pages, along with the main application, CRUD/database files, and multiple CSV datasets used for data practice and application functionality.

---

# 🧩 Application Modules

The Streamlit application is divided into separate functional modules.

```text
app.py
 │
 ├── login.py
 │
 ├── modules/dashboard.py
 │
 ├── modules/add_employee.py
 │
 ├── modules/update_employee.py
 │
 ├── modules/delete_employee.py
 │
 └── modules/search_employee.py
```

This modular structure keeps individual application features separated and makes the project easier to maintain.

---

# 🔄 CRUD Operations

The project includes a dedicated `crud.py` module for employee data operations.

The application supports operations such as:

```text
Create
  ↓
Read
  ↓
Update
  ↓
Delete
  ↓
Search
```

The command-line `ui.py` file also demonstrates employee-management operations including viewing, adding, salary updating, deleting, and searching employees.

---

# 📊 Data Handling

The repository contains multiple CSV datasets used for Python/Pandas data handling and practice.

Examples include:

* Employee datasets
* Customer datasets
* Employee master/update datasets
* Customer bonus data
* Richest-person datasets

These files demonstrate working with CSV data and Python-based data processing.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/aakashset/Pandas-Dashboard.git
```

```bash
cd Pandas-Dashboard
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

If you are installing the core packages manually:

```bash
pip install streamlit pandas
```

Install any additional database dependencies required by the local configuration.

---

# 🗄️ Database Configuration

The project contains database-related code through `database.py` and CRUD functionality through `crud.py`.

Before running the complete application, configure the database connection according to your local MySQL setup.

> ⚠️ Never commit database passwords, API keys, or other sensitive credentials to GitHub.

---

# 🚀 Running the Application

Start the Streamlit application from the project root:

```bash
streamlit run app.py
```

After starting the application, Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🖥️ Application Navigation

After login, the sidebar provides the following navigation:

```text
👨‍💼 Employee Management

├── 📊 Dashboard
├── ➕ Add Employee
├── ✏️ Update Employee
├── 🗑️ Delete Employee
├── 🔎 Search Employee
└── 🚪 Logout
```

This navigation is implemented directly in `app.py`.

---

# 🧪 Example Employee Data

The application works with employee information such as:

```text
Employee ID
Name
Age
Gender
Department
Designation
Salary
City
Joining Date
```

Example:

```text
Employee ID : 101
Name        : John
Age         : 28
Gender      : Male
Department  : IT
Designation : Data Analyst
Salary      : 50000
City        : Chennai
Joining Date: 2025-01-10
```

---

# 📸 Screenshots

Add screenshots of the application here.

### 🔐 Login

*Add your login screenshot here.*

### 📊 Dashboard

*Add your dashboard screenshot here.*

### ➕ Add Employee

*Add your Add Employee screenshot here.*

### 🔎 Search Employee

*Add your Search Employee screenshot here.*

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

* Python programming
* Pandas data handling
* CSV processing
* Streamlit application development
* CRUD operations
* Database connectivity
* Modular Python application design
* Employee data management
* Interactive dashboards

---

# 🚀 Future Enhancements

Possible improvements include:

* 🔐 Secure authentication
* 👥 Role-based access control
* 📊 Advanced analytics
* 📈 Interactive charts
* 🔎 Advanced employee filtering
* 📄 Employee report generation
* 📥 CSV/Excel export
* 🐳 Docker deployment
* ☁️ Cloud deployment
* 🧪 Automated testing

---

# 👨‍💻 Author

**Aakash**

Python | Data Engineering Enthusiast

---

⭐ If you find this project useful, consider starring the repository.

**GitHub Repository:**
https://github.com/aakashset/Pandas-Dashboard
