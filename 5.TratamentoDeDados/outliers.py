from operator import index

import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

#  Filtro básico de idade
df_filtro_basico = df[df['idade'] > 100]
print('Idade maior que 100: ', df_filtro_basico[['nome', 'idade']])

#  Identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print('\nFiltrando outliers com z_score: \n', outliers_z)

#  Filtrando outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]
print('\nFiltrando outliers com z_score menor: \n', df_zscore)

# Identificar outliers com iqr
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('Limites IQR: ', limite_alto, limite_baixo)

#  Filtrando outliers com IQR
outlier_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('\nFiltro idade IQR: \n', outlier_iqr)

#  Filtrar ouliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]
print('\nFiltro idade IQR 2: \n', df_iqr)

#  Outra forma de identificar outliers
limite_baixo = 18
limite_alto = 110
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#  Filtrando endereços invalidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço invalido' if len(x.split('\n')) < 3 else x)
print('Qtd de endereços invalidos: ', (df['endereco'] == 'Endereço invalido').sum())

#  Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome invalido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd de nome invalidos: ', (df['nome'] == 'Nome invalido').sum())

print('\nDados com outliers tratados: \n', df)

#  Salvar dataframe
df.to_csv('clientes_remove_outliers.csv', index=False)
