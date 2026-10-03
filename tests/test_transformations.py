import pandas as pd

from src.transformations import calculate_sales


def test_calculate_sales():

    data = pd.DataFrame({
        "Quantity": [2, 5],
        "Price": [100, 200]
    })

    result = calculate_sales(data)

    assert result["Sales"].tolist() == [200, 1000]