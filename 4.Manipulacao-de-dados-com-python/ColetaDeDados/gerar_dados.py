import pandas as pd
import random
from faker import Faker #  Ferramenta para criar dados fictícios

faker = Faker('pt_BR')

dados_pessoas = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18,60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome':nome,
        'cpf':cpf,
        'idade':idade,
        'data':data,
        'endereco':endereco,
        'estado':estado,
        'pais':pais
    }

    dados_pessoas.append(pessoa)

#  Criar um DataFrame com os dados gerados
df_pessoa = pd.DataFrame(dados_pessoas)
print(df_pessoa)

#  Configurando como o dado vai aparecer
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print(df_pessoa.to_string()) #  head() tail()

df_pessoa.to_csv('clientes.csv')
