import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

#  Remover dados
df.drop('pais', axis=1, inplace=True) # Coluna
df.drop(2, axis=0, inplace=True) # Linha
print('\nDados removido: \n ', df.head())

#  Normalizar campos de texto
df['nome'] = df['nome'].str.title() # Toda letra de início maiúscula
df['endereco'] = df['endereco'].str.lower() # Deixa tudo minusculo
df['estado'] = df['estado'].str.strip().str.upper() # Deixa tudo maiúsculo
print('\nDados normalizados: \n', df.head())

#  Converte tipo de dados
df['idade'] = df['idade'].astype(int)
print('\nTipo de dados: \n', df['idade'].dtypes)

#  Tratar valores nulos (ausentes)
print('\nValor nulos: \n', df.isnull().sum()) # Veja primeiro campos que tem valores nulos
df_fillna = df.fillna(0) # Substitui valores nulos por 0
df_dropna = df.dropna() # Remove registros com valores nulos
df_dropna4 = df.dropna(thresh=4) # Mantém linha se ela tiver pelo menos 4 registros
df = df.dropna(subset=['cpf']) # Remover registros com CPF nulo

print('\nQtd registros nulos com fillna:', df_fillna.isnull().sum().sum())
print('Qtd registros nulos com dropna: ', df_dropna.isnull().sum().sum())
print('Qtd registros nulos com dropna4: ', df_dropna4.isnull().sum().sum())
print('Qtd registros nulos com CPF: ', df.isnull().sum().sum())

#  Outras formas de lidar com valores nulos
df.fillna({'estado':'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

#  Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

#  Tratar dados duplicados
print('\nQtd registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd de registros removendo duplicatas', len(df))

print('\nDados limpos: \n', df)

#  Salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome','cpf','idade','data', 'endereco', 'estado']] # Salvando DF só com campos que vai usar
df_salvar.to_csv('clientes_limpeza.csv', index=False) # Criando novo arquivo a partir do dataframe

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))

