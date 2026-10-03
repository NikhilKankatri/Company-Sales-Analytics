import numpy as np
import pandas as pd


def calculate_sales(df):

    df = df.copy()

    df["Sales"] = df["Quantity"] * df["Price"]

    return df


def create_sales_category(df):

    df = df.copy()

    df["Sales_Category"] = np.where(
        df["Sales"] >= 50000,
        "High Value",
        np.where(
            df["Sales"] >= 10000,
            "Medium Value",
            "Low Value"
        )
    )

    return df