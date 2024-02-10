import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow_hop.operators import HopWorkflowOperator

local_tz=pendulum.timezone('America/Sao_Paulo')

default_args = {
    'owner': 'Paulo',
    'depends_on_past': False,
    #'start_date': datetime.today() - timedelta(days=1),  #datetime(2021, 3, 13, 0, tzinfo=local_tz), datetime(yyyy,mm,dd,hh,mn,sc, tzinfo=local_tz),
    'start_date': datetime(2021, 3, 13, 0, tzinfo=local_tz), #datetime(yyyy,mm,dd,hh,mn,sc, tzinfo=local_tz),
    'email': ['@EMAIL'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    dag_id='dag-workflow-input-hop',
    default_args=default_args,
    schedule_interval='0 3 4-6 * *',
    catchup=False,
    tags=['principal']
)

job = HopWorkflowOperator(
    dag=dag,
    task_id='tsk-workflow-input-hop',
    workflow='INTEGRACAO/workflow-input.hwf',
    project_path='/opt/projetos/live_hop',
    project_name='live_hop',
    environment_path='/opt/projetos/live_hop/env/prd',
    environment_name='hop-live-prd',
    hop_config_path='/opt/projetos/hop_config',
    log_level= 'Basic'
)
