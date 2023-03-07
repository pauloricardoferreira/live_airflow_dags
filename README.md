## Bem-vindo

Neste repositório você vai encontrar 2 exemplos da DAG's para utilizar em projetos com Apache Airflow e Apache Hop

<br>

Páginas Oficiais dos Projetos
 - [Apache Hop](https://hop.apache.org/)
 - [Apache Airflow](https://airflow.apache.org/)

<br>

```python
#importação de bibliotecas básicas
import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow_hop.operators import HopWorkflowOperator

#definição do TimeZone
local_tz=pendulum.timezone('America/Sao_Paulo')

#Arquimenstos Padrão da DAG
default_args = {
    'owner': 'Live',                                            #Dono
    'depends_on_past': False,                                   #Não executa o passado
    'start_date': datetime(2021, 3, 13, 0, tzinfo=local_tz),    #Data de Inicio de Ezecução
    'email': ['admin@gmail.com'],                               #E-mail
    'email_on_failure': False,                                  #Envia e-mail em caso de falha
    'email_on_retry': False,                                    #Envia e-mail em caso de nova tentativa de ezecução
    'retries': 0,                                               #Tentativas de execução caso falhe
    'retry_delay': timedelta(seconds=30)                        #Intervalo entre a falha e nova tentativa
}

#Definição da DAG
dag = DAG(
    dag_id='dag-workflow-1-hop',    #ID da DAG, esse ID é exibido na Aplicação Web do Airflow
    default_args=default_args,      #Carrega os argumentos default
    schedule_interval='@once',      #Intervalo de execução, sintax cron schedule_interval='0 1 * * *'
    catchup=False,                  #Não cria execuções futuras, apenas a próxima a partir da data de inicio
    tags=['docker', 'hop']          #tags para identificação e filtros no Airflow Webserver
)

#Definição da Task
job = HopWorkflowOperator(
    dag=dag,                                #Carrega a DAGs
    task_id='tsk-workflow-1-hop',           #ID da task exibida no Airflow Webserver
    workflow='INTEGRACAO/workflow.hwf',     #Caminho Relativo até o Workflow Hop
    project_name='live_hop',                #Nome do Projeto Hop
    environment='hop-repo-prd',             #Nome do arquivo e variavel utilizada no Hop
    log_level= 'Basic'                      #Tipo de Log
)
```
