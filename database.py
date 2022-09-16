import psycopg2
from config.settings import setting

conn=None
cur=None
try:
    conn=psycopg2.connect(
        host=setting.POSTGRES_SERVER,
        dbname=setting.POSTGRES_DB,
        user=setting.POSTGRES_USER,
        password=setting.POSTGRES_PASSWORD,
        port=setting.POSTGRES_PORT
    )
    print("Connected successfully")
    db_conn=conn.cursor()
except Exception as error:
    print("Database Code error -> ",error)