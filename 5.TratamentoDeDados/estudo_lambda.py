import pandas as pd


#  Função para calcular o cubo de um numero

def cubo_numero(x):
    return x ** 3

#  Expressão, lambda para pegar o cubo de um número
eleva_cubo_lambda = lambda x: x ** 3

print(cubo_numero(2))
print(eleva_cubo_lambda(5))

df = pd.DataFrame({'numeros':[1,2,3,4,5,10]})

df['cubo_funcao'] = df['numeros'].apply(cubo_numero)
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3)
print(df)

