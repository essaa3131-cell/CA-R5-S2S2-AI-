from preprocessing import Read_data_file, Drop_unnecessary_features, Check_data_type
from config import DROP_COLUMNS, dataset

df = Read_data_file(dataset)

if df is not None:
    answer = input(f"Drop these columns: {DROP_COLUMNS}? (y/n): ")
    if answer.lower() == "y":
        df = Drop_unnecessary_features(df, DROP_COLUMNS)
        print("Columns dropped successfully.")

    print("\nData type report:")
    print(Check_data_type(df))
else:
    print("Data could not be loaded — check the file path.")