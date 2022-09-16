from fastapi import FastAPI
import uuid
from datetime import date
from config import DB_USERNAME, DB_PASSWORD, HOST
import psycopg2
from pydantic import BaseModel
from upkeepDb import db_fetchall_get,db_fetchone_get,db_fetch_post

app=FastAPI()


class User(BaseModel):
    username:str
    password:str
    accesstype:str


@app.post('/employeelogin',tags=['Employee Login'])
def employee_login(user:User):
    
    sql="SELECT * FROM USERS where username='%s' and password='%s' and access_type='%s'"%(user.username,user.password,user.access_type)
    data= db_fetchall_get()
    if data and user.access_type != "HR":
        return data 
    else:
        return {"msg":"Employee is Not Registered"}

@app.post('/hrlogin',tags=['HR Login'])
def HR_login(user_name:str,password:str,access_type:str):
    sql="SELECT * FROM USERS where username='%s' and password='%s' and access_type='%s'"%(user_name,password,access_type)
    data= db_conn.fetchall()
    db_conn.close()
    conn.close()
    if data and access_type=='HR':
        return data 
    else:
        return {"msg":"HR is Not Registered"}

@app.get("/users/{user_id}")
def user_data(user_id:str):
    conn=conn=psycopg2.connect(
        host=setting.POSTGRES_SERVER,
        dbname=setting.POSTGRES_DB,
        user=setting.POSTGRES_USER,
        password=setting.POSTGRES_PASSWORD,
        port=setting.POSTGRES_PORT
    )
    db_conn=conn.cursor()
    db_conn.execute("SELECT * FROM EMPLOYEE_MANAGEMENT WHERE EMP_ID='%s'"%(user_id))
    data=db_conn.fetchall()
    db_conn.close()
    conn.close()
    if data:
        return data
    else:
        return {"message":"No user avaliable"} 

@app.post('/emp-data')
def create_employee(email:str,emp_type:str,emp_id:str,password:str):

    conn=conn=psycopg2.connect(
        host=setting.POSTGRES_SERVER,
        dbname=setting.POSTGRES_DB,
        user=setting.POSTGRES_USER,
        password=setting.POSTGRES_PASSWORD,
        port=setting.POSTGRES_PORT
    )
    db_conn=conn.cursor()
    ch=db_conn.execute("select * from employee_management where emp_id='%s' or email='%s'"%(email,emp_id))
    data=db_conn.fetchall()
    conn.close()
    if data:
        return {"message": "User already exist"}
    try:
        management_id=str(uuid.uuid4())
        current_date=date.today()
        #values=(management_id,email,emp_type,emp_id,current_date,password,'active','yet_to_login')
        conn=conn=psycopg2.connect(
        host=setting.POSTGRES_SERVER,
        dbname=setting.POSTGRES_DB,
        user=setting.POSTGRES_USER,
        password=setting.POSTGRES_PASSWORD,
        port=setting.POSTGRES_PORT
        )   
        db_conn=conn.cursor()
        db_conn.execute("insert into employee_management(management_id,email,emp_type,emp_id,date_of_joining,password,emp_status,onboarding_status)values(%s,%s,%s,%s,%s,%s,%s,%s)",(management_id,email,emp_type,emp_id,current_date,password,'active','yet_to_login'))
        conn.commit()
        conn.close()
        return {"message":"Registered"}
    except Exception as error:
        print ("error is ",error)
    finally:
        db_conn.close()