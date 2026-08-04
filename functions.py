import pandas as pd


# -------------------- Read Files --------------------

def read_files():
    df1 = pd.read_csv("employee_master_25.csv")
    df2 = pd.read_csv("employee_updates_25.csv")
    return df1, df2


# -------------------- View Records --------------------

def view_records(df):
    print(df)


# -------------------- Search by Emp_ID --------------------

def search_empid(df):

    empid = int(input("Enter Employee ID : "))

    data = df[df["Emp_ID"] == empid]

    if len(data) > 0:
        print(data)
    else:
        print("Employee Not Found")


# -------------------- Match by Name --------------------

def match_name(df1, df2):

    name = input("Enter Employee Name : ")

    data1 = df1[df1["Name"].str.lower() == name.lower()]
    data2 = df2[df2["Name"].str.lower() == name.lower()]

    if len(data1) > 0:
        print("\nMaster File")
        print(data1)

    if len(data2) > 0:
        print("\nUpdate File")
        print(data2)

    if len(data1) == 0 and len(data2) == 0:
        print("No Matching Record")


# -------------------- Match by Salary --------------------

def match_salary(df1, df2):

    salary = int(input("Enter Salary : "))

    data1 = df1[df1["Salary"] == salary]
    data2 = df2[df2["Salary"] == salary]

    if len(data1) > 0:
        print("\nMaster File")
        print(data1)

    if len(data2) > 0:
        print("\nUpdate File")
        print(data2)

    if len(data1) == 0 and len(data2) == 0:
        print("No Matching Salary")


# -------------------- Update Record --------------------

def update_record(df):

    empid = int(input("Enter Employee ID : "))

    if empid in df["Emp_ID"].values:

        print("\nAvailable Columns")
        print(df.columns)

        column = input("\nEnter Column Name : ")

        if column in df.columns:

            value = input("Enter New Value : ")

            df.loc[df["Emp_ID"] == empid, column] = value

            df.to_csv("employee_master_25.csv", index=False)

            print("Record Updated Successfully")

        else:
            print("Column Not Found")

    else:
        print("Employee ID Not Found")


# -------------------- Add Row --------------------

def add_row(df):

    empid = int(input("Emp_ID : "))
    name = input("Name : ")
    role = input("Role : ")
    salary = int(input("Salary : "))

    df.loc[len(df)] = [empid, name, role, salary]

    df.to_csv("employee_master_25.csv", index=False)

    print("Row Added Successfully")


# -------------------- Add Column --------------------

def add_column(df):

    column = input("Column Name : ")

    value = input("Default Value : ")

    df[column] = value

    df.to_csv("employee_master_25.csv", index=False)

    print("Column Added")


# -------------------- Drop Column --------------------

def drop_column(df):

    column = input("Column Name : ")

    if column in df.columns:

        df.drop(columns=[column], inplace=True)

        df.to_csv("employee_master_25.csv", index=False)

        print("Column Deleted")

    else:
        print("Column Not Found")


# -------------------- Sort --------------------

def sort_records(df):

    order = input("Sort (ASC/DSC) : ").lower()

    if order == "asc":

        df = df.sort_values(by="Emp_ID")

    elif order == "dsc":

        df = df.sort_values(by="Emp_ID", ascending=False)

    else:
        print("Invalid Choice")

    print(df)


# -------------------- Main Program --------------------

while True:

    df1, df2 = read_files()

    print("\n========== EMPLOYEE MANAGEMENT ==========")
    print("1. View Records")
    print("2. Search by Emp_ID")
    print("3. Match by Name")
    print("4. Match by Salary")
    print("5. Update Record")
    print("6. Add Row")
    print("7. Add Column")
    print("8. Drop Column")
    print("9. Sort Records")
    print("10. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        view_records(df1)

    elif choice == "2":
        search_empid(df1)

    elif choice == "3":
        match_name(df1, df2)

    elif choice == "4":
        match_salary(df1, df2)

    elif choice == "5":
        update_record(df1)

    elif choice == "6":
        add_row(df1)

    elif choice == "7":
        add_column(df1)

    elif choice == "8":
        drop_column(df1)

    elif choice == "9":
        sort_records(df1)

    elif choice == "10":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")