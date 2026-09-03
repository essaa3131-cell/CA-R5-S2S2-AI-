import pandas as pd

def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: file not found at this path: {file_path}")
        return None
    except Exception as e:
        print(f"Something went wrong while reading the file: {e}")
        return None
def Drop_unnecessary_features(df, cols_to_drop):
    return df.drop(columns=cols_to_drop)    
def Check_data_type(df):
    dtypes = df.dtypes
    n_unique = df.nunique()
    report = pd.DataFrame({
        "Dtype": dtypes,
        "Num_Unique": n_unique
    })
    return report.T