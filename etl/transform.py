import os
import pandas as pd
from extract import extract_data

PROCESSED_DATA_PATH = "data/processed/cleaned_data.csv"

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
  df = df.copy()
  df = df.drop_duplicates()
  df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ","_")
  )
  df = df.dropna()
  if "order_date" in df.columns:
    df["order_date"] = pd.to_datetime(df["order_date"],errors="coerce")
  if "quantity" in df.columns:
    df["quantity"] = pd.to_numeric(df["quantity"],errors="coerce")
  if "price" in df.columns:
    df["price"] = pd.to_numeric(df["price"],errors="coerce")
  if "quantity" in df.columns and "price" in df.columns:
    df["total_amount"] = df["quantity"] * df["price"]
  df = df.dropna()
  return df

def save_data(df: pd.DataFrame, output_path: str = PROCESSED_DATA_PATH) -> None:
  os.makedirs(os.path.dirname(output_path),exist_ok=True)
  df.to_csv(output_path, index=False)
  print(f"Successfully saved {len(df)} rows to {output_path}.")

if __name__ = "__main__":
  raw_data = extract_data()
  cleaned_data = transform_data(raw_datа)
  save_data(cleaned_data)
