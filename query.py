import os, random
from datetime import datetime
import psycopg2
from dotenv import load_dotenv
load_dotenv('environment/credentials.env')

def consultarPostgres(db, sch, tb):

    conn = psycopg2.connect(
        host=os.getenv('HOST_DL'),
        user=os.getenv('USER_DL'),
        password=os.getenv('PW_DL'),
        port=os.getenv('PORT_DL'),
        database=db,
    )
    order=random.randint(0,1000)
    data=datetime.now()
    data=format(data,'%d/%m/%Y %H:%M:%S')
    print(f'[{data}] LOG [QUERY #{order}]: CONECTADO EM |DB: {db} |SCHEMA: {sch} |TABLE: {tb}')

    column_names = []
    resultado=None
    cs = conn.cursor()

    if db=='pardal':
        cs.execute(f'SELECT * FROM {sch}.{tb} LIMIT 10000 ')
        column_names = [desc[0] for desc in cs.description]
        column_names.append('A CONSULTA FOI LIMITADA A 2 MILHÕES DE RESULTADOS DEVIDO AO SEU TAMANHO REAL SER MAIOR OU IGUAL A 300MB!')
        resultado = cs.fetchall()
    else: 
        cs.execute(f'SELECT * FROM {sch}.{tb}')
        column_names = [desc[0] for desc in cs.description]
        resultado = cs.fetchall()

    conn.close()
    print(f'[{data}] LOG [QUERY #{order}]: Consulta concluida com sucesso e sem erros!')
    return resultado, column_names
