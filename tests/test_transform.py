import pandas as pd
from etl.transform import transform_data

def test_transform_data_adds_total_amount():
    raw_df = pd.DataFrame(
        {
            "order_id": [1001],
            "customer_id": [201],
            "product_id": [501],
            "order_date": ["2026-01-02"],
            "quantity": [2],
            "price": [1499.99],
        }
    )

    cleaned_df = transform_data(raw_df)
    assert "total_amount" in cleaned_df.columns
    assert cleaned_df.loc[0, "total_amount"] == 2999.98

def test_transform_data_removes_duplicates():
    raw_df = pd.DataFrame(
        {
            "order_id": [1001, 1001],
            "customer_id": [201, 201],
            "product_id": [501, 501],
            "order_date": ["2026-01-02", "2026-01-02"],
            "quantity": [2, 2],
            "price": [1499.99, 1499.99],
        }
    )

    cleaned_df = transform_data(raw_df)
    assert len(cleaned_df) == 1

def test_transform_data_normalizes_column_names():
    raw_df = pd.DataFrame(
        {
            "Order ID": [1001],
            "Customer ID": [201],
            "Product ID": [501],
            "Order Date": ["2026-01-02"],
            "Quantity": [2],
            "Price": [1499.99],
        }
    )

    cleaned_df = transform_data(raw_df)
    assert "order_id" in cleaned_df.columns
    assert "customer_id" in cleaned_df.columns
    assert "total_amount" in cleaned_df.columns
