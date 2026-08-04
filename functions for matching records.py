import pandas as pd


# -----------------------------
# Read CSV Files
# -----------------------------
def read_files():
    df1 = pd.read_csv("employees_practice1.csv")
    df2 = pd.read_csv("employees_practice2.csv")
    return df1, df2


# -----------------------------
# Match Records
# -----------------------------
def matching_records(df1, df2):

    print("\nMatch By")
    print("1. Emp_ID")
    print("2. Name")
    print("3. Department")
    print("4. Salary")

    choice = input("Enter your choice : ")

    if choice == "1":
        column = "Emp_ID"
    elif choice == "2":
        column = "Name"
    elif choice == "3":
        column = "Department"
    elif choice == "4":
        column = "Salary"
    else:
        print("Invalid Choice")
        return None

    match = pd.merge(df1, df2, on=column,
                     suffixes=("_File1", "_File2"))

    print("\nTotal Matching Records :", len(match))

    return match


# -----------------------------
# Sort Records
# -----------------------------
def sort_records(df):

    order = input("\nSort (ASC/DSC) : ").lower()

    if order == "asc":
        df = df.sort_values(by=df.columns[0])

    elif order in ["dsc", "desc"]:
        df = df.sort_values(by=df.columns[0], ascending=False)

    else:
        print("Invalid Choice")

    return df


# -----------------------------
# Search Employee
# -----------------------------
def search_employee(df):

    if "Emp_ID" not in df.columns:
        print("\nEmployee ID not available for searching.")
        return

    try:
        empid = int(input("\nEnter Employee ID : "))
    except ValueError:
        print("Enter Numbers Only")
        return

    data = df[df["Emp_ID"] == empid]

    if len(data) > 0:
        print("\nMatching Record\n")
        print(data)
    else:
        print("Employee Not Found")


# -----------------------------
# Print Records
# -----------------------------
def print_records(df):

    ch = input("\nPrint Matching Records? (Yes/No): ").lower()

    if ch == "yes":
        print("\nMatching Records\n")
        print(df)

    else:
        print("Printing Skipped")


# -----------------------------
# Main Program
# -----------------------------
while True:

    df1, df2 = read_files()

    match = matching_records(df1, df2)

    if match is not None:

        match = sort_records(match)

        search_employee(match)

        print_records(match)

    again = input("\nDo you want to continue? (Yes/No): ").lower()

    if again != "yes":
        print("\nProgram Ended")
        break