import pandas as pd


def load_sales_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        print(f"Rows: {len(df)}")
        return df

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except Exception as error:
        print(f"Error loading data: {error}")
        return None