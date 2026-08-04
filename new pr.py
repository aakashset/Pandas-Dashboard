import pandas as pd
import numpy as np

source_file_path = r"D:\learning\PythonProject\PythonProject\customer_bonus.csv"
source_df = pd.read_csv(source_file_path)


source_df.columns = source_df.columns.str.strip().str.lower()

while True:
    action = input("What do you want to do? [add] [remove] [print] [exit]: ").strip().lower()

    if action == "add":
        add_choice = input("What do you want to add? [row] [column]: ").strip().lower()
        if add_choice == "row":
            id_column = None
            for col in source_df.columns:
                if "id" in col:
                    id_column = col
                    break

            if not id_column:
                id_column = "cust id"

            id_choice = input("How to set ID? [manual] [auto]: ").strip().lower()
            if id_choice == "manual":
                id_input = input(f"Enter new {id_column}: ").strip()
                if not id_input.isdigit():
                    print(f"Error: {id_column} must be a number!")
                    continue
                new_id = int(id_input)

                if id_column in source_df.columns and new_id in pd.to_numeric(source_df[id_column],
                                                                              errors='coerce').values:
                    print(f"Error: ID {new_id} already exists!")
                    continue

            elif id_choice == "auto":
                if id_column in source_df.columns and not source_df.empty:
                    valid_ids = pd.to_numeric(source_df[id_column], errors='coerce').dropna()
                    if not valid_ids.empty:
                        new_id = int(valid_ids.max()) + 1
                    else:
                        new_id = 101
                else:
                    new_id = 101
                print(f"Generated ID: {new_id}")
            else:
                print("Invalid option! Returning to main menu.")
                continue

            new_data = {id_column: new_id}

            for col in source_df.columns:
                if col == id_column:
                    continue

                new_val = input(f"Enter value for '{col}': ").strip()

                if "sal" in col:
                    if new_val.replace('.', '', 1).isdigit():
                        new_data[col] = float(new_val)
                    else:
                        print(f"Warning: '{new_val}' is not a valid number for salary. Storing as text.")
                        new_data[col] = new_val
                else:
                    if new_val.isdigit():
                        new_data[col] = int(new_val)
                    else:
                        new_data[col] = new_val

            new_row = pd.DataFrame([new_data])
            source_df = pd.concat([source_df, new_row], ignore_index=True)

            source_df.to_csv(source_file_path, index=False)
            print("Row added and saved successfully to the original file!")

        elif add_choice == "column":
            print("\nOptions for adding a column: [manual] [csv]")
            column_mode = input("Choose an option: ").strip().lower()

            if column_mode not in ["manual", "csv"]:
                print("Invalid column option! Returning to main menu.")
                continue

            if column_mode == "manual":
                new_col_name = input("Enter new column name: ").strip().lower()
                if new_col_name in source_df.columns:
                    print(f"Error: Column '{new_col_name}' already exists!")
                    continue

            source_path = input("Enter the absolute file path of the source CSV to copy from: ").strip().strip(
                '"').strip("'")

            try:
                source_df_ext = pd.read_csv(source_path)
                source_df_ext.columns = source_df_ext.columns.str.strip().str.lower()

                id_column = None
                for col in source_df.columns:
                    if "id" in col:
                        id_column = col
                        break

                if not id_column:
                    print("Error: Could not determine the ID column in your destination file!")
                    continue


                source_id_col = None
                for col in source_df_ext.columns:
                    if "id" in col:
                        source_id_col = col
                        break

                source_cols_list = list(source_df_ext.columns)

                if not source_id_col:
                    print("\nCould not automatically detect an ID column in the source CSV.")
                    print("Columns found inside the source CSV file:")
                    for idx, col in enumerate(source_cols_list, start=1):
                        print(f"[{idx}] {col}")

                    id_select = input(f"Select the number matching your destination '{id_column}': ").strip()
                    if not id_select.isdigit() or int(id_select) < 1 or int(id_select) > len(source_cols_list):
                        print("\n[CRITICAL ERROR]: Primary Key Misalignment Detected!")
                        print("Selection index failed to resolve against mapped columns. Operation aborted.")
                        continue
                    source_id_col = source_cols_list[int(id_select) - 1]
                else:
                    print(
                        f"Automatically matched source key column: '{source_id_col}' to destination key: '{id_column}'")

                if column_mode == "csv":
                    print("\nColumns found inside the source CSV file:")
                    for idx, col in enumerate(source_cols_list, start=1):
                        print(f"[{idx}] {col}")

                    data_select = input("Select the number of the column to copy data from: ").strip()
                    if not data_select.isdigit() or int(data_select) < 1 or int(data_select) > len(source_cols_list):
                        print("Error: Invalid column number selection!")
                        continue
                    source_col = source_cols_list[int(data_select) - 1]

                    new_col_name = source_col
                    if new_col_name in source_df.columns:
                        new_col_name = input(
                            f"Column '{source_col}' already exists in destination. Enter a new name to save it as: ").strip().lower()
                else:
                    print("\nColumns found inside the source CSV file:")
                    for idx, col in enumerate(source_cols_list, start=1):
                        print(f"[{idx}] {col}")

                    data_select = input(
                        f"Select the number of the column to load data into your custom '{new_col_name}': ").strip()
                    if not data_select.isdigit() or int(data_select) < 1 or int(data_select) > len(source_cols_list):
                        print("Error: Invalid column number selection!")
                        continue
                    source_col = source_cols_list[int(data_select) - 1]

                dest_ids = set(pd.to_numeric(source_df[id_column], errors='coerce').dropna().astype(int))
                source_ids = set(pd.to_numeric(source_df_ext[source_id_col], errors='coerce').dropna().astype(int))

                missing_ids = dest_ids - source_ids

                source_df[id_column] = pd.to_numeric(source_df[id_column], errors='coerce')
                source_df_ext[source_id_col] = pd.to_numeric(source_df_ext[source_id_col], errors='coerce')

                id_map = dict(zip(source_df_ext[source_id_col].dropna().astype(int), source_df_ext[source_col]))
                source_df[new_col_name] = source_df[id_column].fillna(-1).astype(int).map(id_map)

                source_df.loc[source_df[id_column].isna() | ~source_df[id_column].astype(int).isin(
                    id_map.keys()), new_col_name] = np.nan

                if missing_ids:
                    print(f"\nWarning: Partial match found!")
                    print(f"Total unmatched IDs: {len(missing_ids)}")
                    print(f"Unmatched IDs: {list(missing_ids)}")
                    print(f"Value 'NaN' printed for these unmatched entries.")
                else:
                    print("\nPerfect match! All IDs matched successfully across both files.")

                source_df.to_csv(source_file_path, index=False)
                print(f"Column '{new_col_name}' successfully added and updated in the original file!")

            except Exception as e:
                print(f"Failed to read or process source file: {e}")
                continue

    elif action == "remove":
        remove_choice = input("What do you want to remove? [row] [column]: ").strip().lower()

        if remove_choice == "row":
            id_column = None
            for col in source_df.columns:
                if "id" in col:
                    id_column = col
                    break

            if not id_column or id_column not in source_df.columns:
                print("Error: No ID column found to identify rows!")
                continue

            target_input = input(f"Enter the {id_column} of the row to remove: ").strip()
            if not target_input.isdigit():
                print("Error: ID must be a number!")
                continue
            target_id = int(target_input)

            if target_id not in pd.to_numeric(source_df[id_column], errors='coerce').values:
                print(f"Error: ID {target_id} not found!")
                continue

            source_df = source_df[pd.to_numeric(source_df[id_column], errors='coerce') != target_id].reset_index(
                drop=True)

            source_df.to_csv(source_file_path, index=False)
            print(f"Row with ID {target_id} removed and original file updated successfully!")

        elif remove_choice == "column":
            print(f"Current columns: {list(source_df.columns)}")
            col_to_remove = input("Enter the exact column name to remove: ").strip().lower()

            if col_to_remove not in source_df.columns:
                print(f"Error: Column '{col_to_remove}' does not exist!")
                continue

            source_df = source_df.drop(columns=[col_to_remove])

            source_df.to_csv(source_file_path, index=False)
            print(f"Column '{col_to_remove}' removed and original file updated successfully!")

        else:
            print("Invalid option! Returning to main menu.")

    elif action == "print":
        print(source_df.to_string(index=False))

    elif action == "exit":
        break

