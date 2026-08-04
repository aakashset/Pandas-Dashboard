from database import get_connection
import mysql.connector
from activity import log_activity

def view_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return employees

def add_employee(emp_id, name, age, gender,
                 department, designation,
                 salary, city, joining_date):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO employee
        (emp_id, name, age, gender, department,
         designation, salary, city, joining_date)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
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
        cursor.execute(sql, values)
        conn.commit()

        log_activity(
            "Added",
            emp_id,
            name
        )

        print("✅ Employee Added Successfully!")



    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()



def update_salary(emp_id, salary):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE employee
    SET salary=%s
    WHERE emp_id=%s
    """

    cursor.execute(sql, (salary, emp_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Salary Updated Successfully!")
    else:
        print("❌ Employee ID Not Found!")

    cursor.close()
    conn.close()

def delete_employee(emp_id):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM employee
    WHERE emp_id=%s
    """

    cursor.execute(sql, (emp_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Employee Deleted Successfully!")
    else:
        print("❌ Employee ID Not Found!")

    cursor.close()
    conn.close()


def search_employee(emp_id):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM employee
    WHERE emp_id=%s
    """

    cursor.execute(sql, (emp_id,))
    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    return employee


def update_employee(emp_id, name, age, gender,
                    department, designation,
                    salary, city, joining_date):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE employee
    SET
        name=%s,
        age=%s,
        gender=%s,
        department=%s,
        designation=%s,
        salary=%s,
        city=%s,
        joining_date=%s
    WHERE emp_id=%s
    """

    values = (
        name,
        age,
        gender,
        department,
        designation,
        salary,
        city,
        joining_date,
        emp_id
    )

    cursor.execute(sql, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Employee Updated Successfully!")
    else:
        print("❌ Employee ID Not Found!")

    cursor.close()
    conn.close()

