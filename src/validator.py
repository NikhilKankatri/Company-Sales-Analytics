import pandas as pd


def validate_columns(df):
    required_columns = [
        "Order_ID",
        "Customer",
        "Product",
        "Quantity",
        "Price"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        print("Missing columns:", missing_columns)
        return False

    return True


def validate_values(df):
    issues = {}

    issues["duplicate_orders"] = df["Order_ID"].duplicated().sum()
    issues["missing_customer"] = df["Customer"].isna().sum()
    issues["missing_product"] = df["Product"].isna().sum()

    return issues