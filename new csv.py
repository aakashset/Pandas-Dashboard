import pandas as pd

# To read new csv file
df = pd.read_csv(r"D:\learning\PythonProject\PythonProject\TopRichestInWorld.csv")
print(df)
# To show max column_stack
pd.set_option('display.max_columns', None)
print(df)
# # To insert new rows
# df = pd.read_csv("topRichestInWorld.csv")
# print(df)
# n_rows = pd.DataFrame({
#     "Name": ["Aakash", "Dinesh"],
#     "NetWorth": ["5 Billion", "3 Billion"],
#     "Age": [28, 30],
#     "Country/Territory": ["India", "India"],
#     "Source": ["Technology", "Real Estate"],
#     "Industry": ["Technology", "Real Estate"]
# })
# df = pd.concat([df,n_rows], ignore_index=True)
# df.to_csv("TopRichestInWorld.csv", index=False)
# print(df)
# print(df.tail(5))
# To update age using index
# df = pd.read_csv("topRichestInWorld.csv")
# df.loc[99,"Age"] = 78
# df.loc[100,"Age"] = 65
# df.to_csv("TopRichestInWorld(1).csv", index=False)
# print(df)
# print(df.loc[[99,100]])
# to delete duplicates
# df = pd.read_csv("TopRichestInWorld(1).csv")
# df = df.drop_duplicates()
# df.to_csv("TopRichestInWorld(1).csv", index=False)
# print(df)

# while loop to get input
import pandas as pd
# while True:
#     df = pd.read_csv("TopRichestInWorld(1).csv")
#     print("\n -MENU- ")
#     print("1. View Person Details")
#     print("2. Add Record")
#     print("3. Update Age")
#     print("4. Delete Record")
#     print("5. Exit")
#
#     choice = input("\nEnter your choice (1-5): ")
#
#     if choice == "1":
#         print("\nAvailable Records")
#         print(df[["Name"]])
#         index = int(input("\nEnter Index to View Details: "))
#
#         if index in df.index:
#             print("\nPerson Details")
#             print(df.loc[index])
#         else:
#             print("Invalid Index")
#
#     elif choice == "2":
#         print("\nEnter New Person Details")
#         name = input("Enter Name: ")
#         networth = input("Enter Net Worth: ")
#         age = int(input("Enter Age: "))
#         country = input("Enter Country/Territory: ")
#         source = input("Enter Source: ")
#         industry = input("Enter Industry: ")
#
#         df.loc[len(df)] = [
#             name,
#             networth,
#             age,
#             country,
#             source,
#             industry
#         ]
#
#         df.to_csv("TopRichestInWorld(1).csv", index=False)
#
#         print("\nRecord Added Successfully!")
#     elif choice == "3":
#         print("\nAvailable Records")
#         print(df[["Name"]])
#         index = int(input("\nEnter Index to Update: "))
#
#         if index in df.index:
#
#             new_age = int(input("Enter New Age: "))
#             df.loc[index, "Age"] = new_age
#             df.to_csv("TopRichestInWorld(1).csv", index=False)
#             print("\n Age Updated Successfully")
#
#         else:
#             print("Invalid Index")
#
#
#     elif choice == "4":
#
#         print("\nAvailable Records")
#         print(df[["Name"]])
#         index = int(input("\nEnter Index to Delete: "))
#
#         if index in df.index:
#
#             df = df.drop(index)
#
#             df.to_csv("TopRichestInWorld(1).csv", index=False)
#
#             print("\n Record Deleted Successfully")
#
#         else:
#             print("Invalid Index")
#
#
#     elif choice == "5":
#
#         print("\n Exit")
#         break
#
#
#     else:
#
#         print("\n Invalid Choice.enter a number between 1 and 5")

# df = pd.read_csv("TopRichestInWorld(1).csv")
# print(df)