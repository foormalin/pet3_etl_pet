import pandas as pd
import pytest
from etl.extract import extract_data

def test_extract_data_success(tmp_path):
    file_path = tmp_path / "input.csv"
    file_path.write_text(
        "order_id,customer_id,product_id,order_date,quantity,price\n"
        "1001,201,501,2026-01-02,2,1499.99\n"
    )

    df = extract_data(str(file_path))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert "order_id" in df.columns

def test_extract_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_data("wrong/path/input.csv")

def test_extract_data_empty_file(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    with pytest.raises(Exception):
        extract_data(str(file_path))
