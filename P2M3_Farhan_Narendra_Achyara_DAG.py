import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from elasticsearch import Elasticsearch, helpers

import pandas as pd
import psycopg2 as db

def fetchPostgre():
    '''
    Fungsi ini bertujuan untuk mengambil data dari PostgreSQL, package yang digunakan untuk mengambil data ini adalah
    menggunakan psycopg2. Tidak ada input yang diberikan. Output yang didapat adalah raw data berupa csv.
    '''
    conn = db.connect(
        database="airflow",
        user="airflow",
        password="airflow",
        host="postgres",  # Or the IP address of your database server
        port="5432"
    )

    df=pd.read_sql("SELECT * From global_superstore_data",con=conn)
    df.to_csv('/opt/airflow/dags/P2M3_Farhan_Narendra_Achyara_raw_data.csv')
    print('data saved')
    conn.close()

default_args = {
    'owner': 'Farhan',
    'start_date': dt.datetime(2025, 11, 24, 12 ,50)-timedelta(hours=7),
    'retries': 8,
    'retry_delay': dt.timedelta(minutes=30),
}

def clean_data():
    '''
    Fungsi ini bertujuan untuk manipulasi data menggunakan pandas di python, package yang digunakan untuk cleaning data ini adalah
    menggunakan pandas. Data yang akan dimanipulasi diantara lain menggunakan huruf kecil pada kolom, mengisi missing value, dan drop data yang duplikat.
    Tidak ada input yang diberikan. Output yang didapat adalah clean data berupa csv.
    '''
    df = pd.read_csv('/opt/airflow/dags/P2M3_Farhan_Narendra_Achyara_raw_data.csv')

    # Normalisasi nama kolom
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(' ', '')
        .str.replace(r'[^a-zA-Z0-9_]', '', regex=True)
    )

    # Hapus duplikat
    df = df.drop_duplicates()

    # Handling missing values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('unknown')
        else:
            df[col] = df[col].fillna(0)

    df.to_csv('/opt/airflow/dags/P2M3_Farhan_Narendra_Achyara_data_clean.csv', index=False)
    print("✔ Data cleaning selesai")


def post_elastic():
    '''
    Fungsi ini bertujuan untuk memasukkan data ke elasticsearch dengan port elasticsearch 9200. Port tersebut berfungsi untuk memindahkan data ke elasticsearch.
    Package yang digunakan untuk mengambil data ini adalah airflow. Tidak ada input yang diberikan
    Output yang didapat adalah clean data yang masuk ke elasticsearch. 
    '''
    df = pd.read_csv('/opt/airflow/dags/P2M3_Farhan_Narendra_Achyara_data_clean.csv')

    es = Elasticsearch("http://elasticsearch:9200") #or pi {127.0.0.1}
    actions = [
        {
        "_index": "milestone3",
        "_source": r.to_dict()
        }
        for i,r in df.iterrows()
            # or for i,r in df.iterrows()
    ]

    response = helpers.bulk(es, actions)
    print(response)


with DAG('filter_from_postgre',
         default_args=default_args,
         schedule_interval= '0-59 * * * *',  
         catchup = False    
         ) as dag:

    print_starting = BashOperator(task_id='starting',
                               bash_command='echo "Connnecting to postgresql....."')

    fetch_data = PythonOperator(task_id='fetch_from_postgre',
                                 python_callable=fetchPostgre)
    
    transform_data = PythonOperator(task_id = 'transform_data',
                                    python_callable = clean_data)
    
    insert_elasticsearch = PythonOperator(task_id = 'insert_to_elasticsearch',
                                          python_callable = post_elastic)

print_starting >> fetch_data
fetch_data  >> transform_data
transform_data >> insert_elasticsearch