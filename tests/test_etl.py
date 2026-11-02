import pandas as pd
from etl import transform_data


def test_remove_duplicates():

    data = {
        "OrderID": [101, 101, 102],
        "Customer": ["John", "John", "David"],
        "Product": ["Laptop", "Laptop", "Mouse"],
        "Quantity": [2, 2, 5],
        "Price": [1200, 1200, 20],
        "City": ["Colombo", "Colombo", "Kandy"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert len(result) == 2


def test_remove_missing_values():

    data = {
        "OrderID": [101, 102],
        "Customer": ["John", "David"],
        "Product": ["Laptop", "Mouse"],
        "Quantity": [2, None],
        "Price": [1200, 20],
        "City": ["Colombo", "Kandy"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert len(result) == 1


def test_total_sales_calculation():

    data = {
        "OrderID": [101],
        "Customer": ["John"],
        "Product": ["Laptop"],
        "Quantity": [2],
        "Price": [1200],
        "City": ["Colombo"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert result["TotalSales"].iloc[0] == 2400
