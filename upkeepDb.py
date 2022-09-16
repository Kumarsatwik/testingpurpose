import psycopg2
from config import DB_USERNAME, DB_PASSWORD, HOST
from psycopg2.extras import RealDictCursor
import os


def db_fetchall_get(sql):
    conn = psycopg2.connect(database="upkeep", user=DB_USERNAME,password=DB_PASSWORD, host=HOST, port="25060")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    conn.close()
    return data


def db_fetchone_get(sql):
    conn = psycopg2.connect(database="upkeep", user=DB_USERNAME,password=DB_PASSWORD, host=HOST, port="25060")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchone()
    conn.close()
    return data


def db_fetch_post(sql):
    conn = psycopg2.connect(database="upkeep", user=DB_USERNAME,password=DB_PASSWORD, host=HOST, port="25060")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return True