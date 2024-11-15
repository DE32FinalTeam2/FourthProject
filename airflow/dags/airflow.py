from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
with DAG(
    'data',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(seconds=3)
    },
    description='hello world DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 11, 12),
    catchup=True,
    tags=['simple', 'bash', 'etl', 'shop'],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    task_date = BashOperator(
            task_id='print.date',
            bash_command="""
                echo "date => date"
                echo "ds => {{ds}}"
                echo "ds_nodash => {{ds_nodash}}"
                echo "logical_date => {{logical_date}}"
                echo "logical_date => {{logical_date.strftime("%Y-%m-%d %H:%M:%S")}}"
                echo "execution_date => {{execution_date}}"
                echo "execution_date => {{execution_date.strftime("%Y-%m-%d %H:%M:%S")}}"
                echo "next_execution_date => {{next_execution_date.strftime("%Y-%m-%d %H:%M:%S")}}"
                echo "prev_execution_date => {{prev_execution_date.strftime("%Y-%m-%d %H:%M:%S")}}"
                echo "ts => {{ts}}"
        """
    )

    task_start = EmptyOperator(task_id='start')
    task_end = EmptyOperator(task_id='end', trigger_rule="all_done")

    task_start >> task_date >> task_end


