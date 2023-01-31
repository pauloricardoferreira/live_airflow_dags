import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow_hop.operators import HopWorkflowOperator

local_tz=pendulum.timezone('America/Sao_Paulo')

default_args = {
    'owner': 'Agroterenas',
    'depends_on_past': False,
    'start_date': datetime.today() - timedelta(days=1),  #datetime(2021, 3, 13, 0, tzinfo=local_tz), datetime(yyyy,mm,dd,hh,mn,sc, tzinfo=local_tz),
    'email': ['admin@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    dag_id='dag-workflow-1-hop-hpl',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False,
    tags=['docker', 'hop']
)

job = HopWorkflowOperator(
    dag=dag,
    task_id='tsk-workflow-1-hop-hpl',
    workflow='INTEGRACAO/pipeline.hpl',
    project_name='LIVE',
    pipeline_configuration='pipeline-server',
    log_level= 'Basic'
)
