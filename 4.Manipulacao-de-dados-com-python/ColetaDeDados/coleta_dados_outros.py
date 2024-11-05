from operator import index

import pymysql
import pandas as pd
from sqlalchemy import create_engine

def conexao_mysql(host, user, password, db, table):
    #  Criar conexão
    conn = pymysql.connect(host=host, user=user, password=password, db=db)

    cursor = conn.cursor() # Serve para conectar

    #  Executar consulta
    query = 'select * from ' + table + ' limit 10'
    cursor.execute(query)

    resultados = cursor.fetchall()

    #  Exibir os resultados
    print('Tabela MySql: ')
    for linha in resultados:
        print(linha)

    #  Fechar a conexão, sempre fechar
    cursor.close()
    conn.close()

def df_conexao_mysql(host, user, password, db, table):
    #  Criar conexao
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)
    # conn = pymysql.connect(host=host, user=user, password=password, db=db) - forma usável

    #  Execultar consulta
    query = 'select * from ' + table
    df = pd.read_sql(query, conn)

    # Mostrar resultados
    print('Tabela: \n',df)

    #  Fechar conexão
    # conn.close()
    conn.dispose()

    #  Retorna o valor do arquivo
    return df

def conexao_excel(path):
    #  Ler arquivo
    df = pd.read_excel(path)
    print('Dados Excel: \n', df.head())

    #  Escrever arquivo CSV
    df.to_csv('dados.csv', index=False)

def conexao_csv(param):
    # Ler arquivo CSV
    df = pd.read_csv(param)
    print('Dados CSV: \n ', df)

    df.to_json('dados.json', orient='records', index=False)

df_cliente = df_conexao_mysql('localhost', 'root', '44192919Mc', 'informatica', 'cliente')
df_cliente.to_excel('dados.xlsx', index=False)
# conexao_mysql('localhost', 'root', '44192919Mc', 'informatica', 'cliente')

conexao_excel('dados.xlsx')

conexao_csv('dados.csv')