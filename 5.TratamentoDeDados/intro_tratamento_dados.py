import pandas as pd

df = pd.read_csv('clientes.csv')

#  Verifica primeiros registros
print('Início: ',df.head().to_string()) # Por padrão pega os 5 primeiros

#  Verifica ultimo registros
print('Fim: ', df.tail().to_string()) #  Por padrão pega as 5 ultimas

#  Verificar quantidade de linhas e colunas
print('Qtd de linhas e colunas', df.shape)

#  Verificar tipo de dados
print('Tipo do dado: \n', df.dtypes)

#  Contar valores nulos
print('Valores nulos: \n', df.isnull().sum())