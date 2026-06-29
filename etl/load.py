from sqlalchemy import create_engine
from transform import transform_data
from extract import extract_data

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "de_project"

TABLE_NAME = "sales"

def load_data():
  df = transform_data(extract_data())
  engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
  )
  df.to_sql(
    TABLE_NAME,
    engine,
    if_exists="replace",
    index=False
  )
  print(f"Successfully loaded {len(df)} rows into '{TABLE_NAME}'.")

if __name__ = "__main__":
  load_date()

