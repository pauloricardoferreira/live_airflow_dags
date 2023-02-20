## Conteúdo do repositório
___

<br>

- ### Pasta airflow_hop
    aqui contem o pluguin utilizado para que o Apache Airfloe se comunica com o Apache Hop

<br>

### Exemplo de DAG com comentários

```python
import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow_hop.operators import HopWorkflowOperator

local_tz=pendulum.timezone('America/Sao_Paulo')

default_args = {
    'owner': 'Empresa', #Dono 
    'depends_on_past': False,
    'start_date': datetime.today() - timedelta(days=1),  #desta forma o airfloe entende que precisa ser criado a execução a partir do dia anterior da publicação
    #'start_date': datetime(2021, 3, 13, 0, tzinfo=local_tz), datetime(yyyy,mm,dd,hh,mn,sc, tzinfo=local_tz),
    #o parametro start_date acima, é normalmente utilizado, dessa forma o Airflow criar diversas agendamentos a partir dessa data
    'email': ['admin@gmail.com'],
    'email_on_failure': False, #caso a execução falhe, envia um email -> é necessário configurar na interface
    'email_on_retry': False, #caso a execução execute novamente após a falha, envia um email -> é necessário configurar na interface
    'retries': 0, #numero de tentativas em caso de falha
    'retry_delay': timedelta(seconds=30) #tempo par uma nova tentativa de execução
}

dag = DAG(
    dag_id='dag-workflow-2-hop', #nome da DAG
    default_args=default_args, #argumentos definidos acima
    schedule_interval='0 1 * * *', #agendamento -> par amais detalhes visite https://crontab.guru/
    catchup=False, #este parametro não permite que o airflow cria uma sequência de execuções
    tags=['docker', 'hop'] #tag para melhor identificação dos processos e também para filtrar
)

job = HopWorkflowOperator(
    dag=dag,
    task_id='tsk-workflow-2-hop', #nome da task
    workflow='INTEGRACAO/workflow.hwf', #caminho relativo até o artefato Hop
    project_name='LIVE', #nome do projeto, que é utilizado para encontrar as variaveis utilizadas no ambiente
    environment: "hop-live-prd", #nome do arquivo onde contém as variáveis de configuração do projeto
    log_level= 'Basic' #nível do log
)
```

- Arquivos DAGS
    workflow-1-hop.py, workflow-2-hop.py