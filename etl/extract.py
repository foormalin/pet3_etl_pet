import os
import pandas as pd

RAW_DATA_PATH = "data/raw/input.csv"

def extract_data(file_path: str = RAW_DATA_PATH) -> pd.DataFrame:
  if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file-path}")
  df = pd.read_csv(file_path)
  if df.empty:
    raise ValueError("Input file is empty")
  print(f"Successfully extracted {len(df)} rows.")
  return df

if __name__ == "__main":
  data = extract_data()
  print(data.head())
