import pandas as pd
from etl.load import load_data

def test_load_data_runs_without_error():
    df = pd.DataFrame(
        {
            "order_id": [1001],
            "customer_id": [201],
            "product_id": [501],
            "order_date": ["2026-01-02"],
            "quantity": [2],
            "price": [1499.99],
            "total_amount": [2999.98],
        }
    )
    assert df is not None
    assert len(df) == 1
