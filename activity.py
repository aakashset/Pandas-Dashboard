from database import get_connection


def log_activity(action, emp_id, employee_name):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO activity_log (action, emp_id, employee_name)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (action, emp_id, employee_name))
    conn.commit()

    cursor.close()
    conn.close()


def get_recent_activity():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM activity_log
        ORDER BY action_time DESC
        LIMIT 10
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data