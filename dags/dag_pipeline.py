"""
=======================================================================================================================
This program automates several tasks, including data transformation and loading data from PostgreSQL to Elasticsearch. 
The dataset contains information on bicycle sales across various countries and continents from 2013 to 2023.
=======================================================================================================================
"""

# Import Libraries
import pandas as pd
import psycopg2 as db
import pendulum
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def fetch_from_postgresql():
    """
    Fetch data from a PostgreSQL database and save it as a CSV file.

    This function connects to the PostgreSQL database using parameters defined in 'conn_string'.
    It executes a query to fetch all data from the 'bike_sales_table' table and saves the data in CSV format
    at '/opt/airflow/data/data_raw.csv'.

    Parameters:
    None

    Returns:
    None - The data is saved as a CSV file without returning any value.

    Example usage:
    fetch_from_postgresql()
    """
    conn_string = "dbname='bike_sales_database' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    
    # Fetch data from PostgreSQL
    df = pd.read_sql('SELECT * FROM bike_sales_table;', conn)
    df.to_csv('/opt/airflow/data/data_raw.csv', index=False)
    conn.close()

def data_cleaning():
    """
    Clean raw data fetched from the PostgreSQL database and save the results as a CSV file.

    The cleaning process includes:
    1. Removing duplicates.
    2. Normalizing column names to lowercase.
    3. Handling missing values in the 'insurance' column by replacing 'None' or NaN with 'No Insurance'.
    4. Adding a unique identifier column, 'id_transaction', with sequential values.
    5. Removing redundant columns ('day', 'month', 'year') that overlap with 'date'.

    After cleaning, the data is saved in CSV format at '/opt/airflow/data/data_clean.csv'.
    A confirmation message "Data cleaned and saved to CSV." is displayed upon successful processing.

    Parameters:
    None

    Returns:
    None - The cleaned data is saved as a CSV file without returning any value.

    Example usage:
    data_cleaning()
    """
    df = pd.read_csv('/opt/airflow/data/data_raw.csv')

    # 1. Drop duplicates
    df.drop_duplicates(inplace=True)

    # 2. Normalize column names
    df.columns = df.columns.str.lower()

    # 3. Handle missing values
    df['insurance'] = df['insurance'].replace('None', 'No Insurance').fillna('No Insurance')

    # 4. Drop redundant columns
    df.drop(['day', 'month', 'year'], axis=1, inplace=True)

    # 5. Add unique identifier column
    df['datedump'] = df['date'].str.replace('-', '')
    df['scdump'] = df['shipping_cost'].astype(str).str.replace('.', '')

    df['id_transaction'] = 'ID' + (df.index + 1).astype(str) + '-' + df['datedump'] + '_' + df['scdump']
    df.drop(['datedump', 'scdump'], axis=1, inplace=True)

    columns = ['id_transaction'] + [col for col in df.columns if col != 'id_transaction']
    df = df[columns]

    # 6. Change 'date' data type
    df['date'] = pd.to_datetime(df['date'])

    # Save the cleaned data to a CSV file
    df.to_csv('/opt/airflow/data/data_clean.csv', index=False)
    print("Data cleaned and saved to CSV.")

def post_to_elasticsearch():
    """
    Load cleaned data into Elasticsearch.

    This function performs the following steps:
    1. Connects to Elasticsearch using specified host and port.
    2. Reads cleaned data from the CSV file located at '/opt/airflow/data/data_clean.csv'.
    3. Converts each row into a dictionary and prepares it for indexing.
    4. Uses the `bulk` function from Elasticsearch to index all data into the 'bike_sales_data' index.
    5. Displays a confirmation message "Successfully load cleaned data to Elasticsearch." upon successful indexing.

    Parameters:
    None

    Returns:
    None - The data is indexed into Elasticsearch without returning any value.

    Example usage:
    post_to_elasticsearch()
    """
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200, 'scheme': 'http'}])
    df = pd.read_csv('/opt/airflow/data/data_clean.csv')

    actions = [
        {
            "_index": "bike_sales_data",
            "_source": r.to_dict()
        }
        for _, r in df.iterrows()
    ]

    # Bulk indexing
    bulk(es, actions)
    print("Successfully load cleaned data to Elasticsearch.")

# DAG configuration
local_tz = pendulum.timezone("Asia/Jakarta")
default_args = {
    'owner': 'Ferryansa',
    'start_date': local_tz.datetime(2024, 11, 1),
    'retries': 1
}

with DAG('dag_pipeline',
         description='A DAG to automate fetching raw data from PostgreSQL, cleaning it, and loading cleaned data to Elasticsearch',
         default_args=default_args,
         schedule_interval='10,20,30 9 * * 6',
         catchup=False
         ) as dag:
    
    # Define tasks
    fetch_data = PythonOperator(
        task_id='fetch_from_postgresql', 
        python_callable=fetch_from_postgresql
    )

    clean_data = PythonOperator(
        task_id='data_cleaning', 
        python_callable=data_cleaning
    )

    post_to_elastic = PythonOperator(
        task_id='post_to_elasticsearch', 
        python_callable=post_to_elasticsearch
    )

    # Task dependencies
    fetch_data >> clean_data >> post_to_elastic
