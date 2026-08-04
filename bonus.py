import pandas as pd

customer_file = "customers(1).csv"
bonus_file = "customer_bonus(1).csv"

df = pd.read_csv(customer_file)
bonus_df = pd.read_csv(bonus_file)


# ---------------- ADD CUSTOMER ----------------
def add_customer():
    mode = input("ID (auto/manual): ").lower()

    if mode == "auto":
        cust_id = df["Cust_ID"].max() + 1
    else:
        cust_id = int(input("Enter Customer ID : "))

    name = input("Enter Name : ")
    salary = float(input("Enter Salary : "))

    df.loc[len(df)] = [cust_id, name, salary]
    df.to_csv(customer_file, index=False)
    print("Customer Added Successfully.")


# ---------------- UPDATE BONUS ----------------
def update_bonus():
    global df

    bonus = bonus_df.rename(columns={"Name": "Name", "Bonus": "Bonus"})

    df = df.merge(bonus, on="Name", how="left")

    df.to_csv(customer_file, index=False)
    print("Bonus Updated Successfully.")


# ---------------- REMOVE CUSTOMER ----------------
def remove_customer():
    global df

    cust_id = int(input("Enter Customer ID : "))
    df = df[df["Cust_ID"] != cust_id]

    df.to_csv(customer_file, index=False)
    print("Customer Removed.")



def print_data():
    print(df)

while True:

    print("\n----- MENU -----")
    print("1. Add Customer")
    print("2. Update Bonus")
    print("3. Remove Customer")
    print("4. Print")
    print("5. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":
        add_customer()

    elif ch == "2":
        update_bonus()

    elif ch == "3":
        remove_customer()

    elif ch == "4":
        print_data()

    elif ch == "5":
        break

    else:
        print("Invalid Choice")