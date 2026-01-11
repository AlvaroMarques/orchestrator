from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id="core_workflow",
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:

    BashOperator(
        task_id="print_date",
        bash_command="date",
    )
