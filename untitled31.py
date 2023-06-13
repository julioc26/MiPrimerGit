import pymysql
import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta
import random

################ MySQL ###################
database = 'mibd'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)
cursor = db.cursor()

def consulta():
    consulta = "SELECT ciudad, adjetivo FROM centrodetrabajo"
    lista = ["Fácil", "Hostil", "Sutil", "Sencillo", "Infantil", "Civil", "Fragil", "Viril", "Útil", "Gentil", "Pueril", "Subtil", "Versátil", "Reptil", "Fébril", "Sutil", "Volátil", "Ágil", "Inútil", "Estéril"]
    print("consulta:", consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    print("type(df)=", type(df))
    print("df.info()=", df.info())
    print("df.describe()=", df.describe())
    print("df.head(10)=", df.head(10))
    print("df.tail(10)=", df.tail(10))
    adjetivos = random.choices(lista, k=len(df))  
    df['ciudad'] = df['ciudad'].map(lambda x: x + " " + random.choice(lista)) 
    df_pivot = df.pivot(columns='ciudad', values='adjetivo')  # Crear la tabla pivotante
    df_pivot.to_excel('df.xlsx', index=False) 
    print("df_pivot:")
    print(df_pivot)

consulta()