# creating csv file
import pandas as pd
#data = {
#  "Emp_ID": [101, 102, 103],   "Name": ["Aakash", "Rahul", "Priya"],
# "Salary": [50000, 60000, 55000]
#}
#df = pd.DataFrame(data)
#df.to_csv("emp.csv", index=False)
#print("CSV file created successfully!")

#for getting particular data of emp using index
#Df = pd.read_csv("emp.csv")
#print(df.loc[1,"Name"])

#for updating salary
# df = pd.read_csv("emp.csv")
# df.loc[df["Name"] == "rahul","salary"] = 80000
# df.to_csv("emp.csv",index=False)
# print(df)
# adding new emp
# df = pd.read_csv("emp.csv")
# new_employee = pd.DataFrame({ "Emp_ID": [104], "Name": ["John"], "Salary": [70000] })
# df = pd.concat([df, new_employee], ignore_index=True)
# print(df)
# df = pd.read_csv("emp.csv")
# emp_id = int(input("Enter Employee ID: "))
# name = input("Enter Employee Name: ")
# salary = int(input("Enter Salary: "))
#
# df.loc[len(df)] = [emp_id, name, salary]
#
# df.to_csv("emp.csv", index=False)
# print(df)
# df = pd.read_csv("emp.csv")
# print(df.columns)
# print(df)
# for deleting duplicte or extra column
# df = pd.read_csv("emp.csv")
# df = df.drop(columns=["salary"])
# print(df)

#To read new csv
import pandas as pd
df = pd.read_csv(r"C:\Users\Hedwig\Downloads\TopRichestInWorld.csv")
print(df)
# To display max columns
pd.set_option('display.max_columns', None)
print(df)



# df.head(10)
# df.tail(10)
# df.info()





