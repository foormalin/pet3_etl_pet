from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from etl.extract import extract_data
from etl.transform import transform_data, save_data
from etl.load import load_data


def extract_task(**context):
    df = extract_data()
    context["ti"].xcom_push(key="raw_data", value=df.to_json())


def transform_task(**context):
    raw_data = context["ti"].xcom_pull(
        key="raw_data",
        task_ids="extract"
    )
    import pandas as pd
    df = pd.read_json(raw_data)
    cleaned_df = transform_data(df)
    save_data(cleaned_df)
    context["ti"].xcom_push(
        key="cleaned_data",
        value=cleaned_df.to_json()
    )

def load_task(**context):
    cleaned_data = context["ti"].xcom_pull(
        key="cleaned_data",
        task_ids="transform"
    )
    import pandas as pd
    df = pd.read_json(cleaned_data)
    load_data(df)

default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_task,
    )
    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_task,
    )
    load = PythonOperator(
        task_id="load",
        python_callable=load_task,
    )

    extract >> transform >> load
