from operator import index

import pandas as pd
import numpy as np

from limpeza_dados import df_salvar

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes_remove_outliers.csv')

print(df.head())

#  Mascara dados pessoais
df['cpf_mascarado'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')
print(df)

#  Corrigir datas
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')
print(df)

#  Corrigindo campo de data
data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))# Where é uma forma de aplicar condições
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan # np.nam atribui valo nulo

#  Corrigir campos com múltiplas informações
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')

#  Verificando a formatação do endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço invalido' if len(x) > 50 or len(x) < 5 else x)

#  Corrigindo dados errados
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido')

#  Corrigindo siglas
estados_br = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
df['estado_sigla'] = df['estado_sigla'].str.upper().apply(lambda x: x if x in estados_br else 'Desconhecido')

print('\nDados tratados: ', df.head())

df['cpf'] = df['cpf_mascarado']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']
df_salvar = df[['nome','cpf','idade','data', 'endereco','bairro','estado']]
df_salvar.to_csv('clientes_tratados.csv', index=False)