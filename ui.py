from crud import *

while True:

    print("\n===== EMPLOYEE MANAGEMENT =====")

    print("1. View Employees")
    print("2. Add Employee")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        employees = view_all()

        print()

        for emp in employees:
            print(emp)

    elif choice == "2":

        emp_id = int(input("Employee ID : "))
        name = input("Name : ")
        age = int(input("Age : "))
        gender = input("Gender : ")
        department = input("Department : ")
        designation = input("Designation : ")
        salary = float(input("Salary : "))
        city = input("City : ")
        joining_date = input("Joining Date (YYYY-MM-DD) : ")

        add_employee(
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

    elif choice == "3":

        emp_id = int(input("Employee ID : "))
        salary = float(input("New Salary : "))

        update_salary(emp_id, salary)

    elif choice == "4":

        emp_id = int(input("Employee ID : "))

        delete_employee(emp_id)

    elif choice == "5":

        emp_id = int(input("Employee ID : "))

        employee = search_employee(emp_id)

        if employee:
            print("\n===== Employee Details =====")
            print(f"ID          : {employee[0]}")
            print(f"Name        : {employee[1]}")
            print(f"Age         : {employee[2]}")
            print(f"Gender      : {employee[3]}")
            print(f"Department  : {employee[4]}")
            print(f"Designation : {employee[5]}")
            print(f"Salary      : ₹{employee[6]}")
            print(f"City        : {employee[7]}")
            print(f"Joining Date: {employee[8]}")
        else:
            print("\n❌ Employee Not Found!")

    elif choice == "6":

        print("Thank You")
        break

    else:

        print("Invalid Choice")