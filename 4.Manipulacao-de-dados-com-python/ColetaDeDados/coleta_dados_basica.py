import requests #  Faze requisição http
from bs4 import BeautifulSoup #  Cria uma árvore de ánalise de páginas para extrair dados mais eficientemente
import pandas

url = 'https://br.financas.yahoo.com/quote/%5EBVSP/history/'

print('-- Request --')
response = requests.get(url)
print(response.text[:600])

print('-- BeautifulSoup --')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print('-- Pandas --')
url_dados = pandas.read_html(url)
print(url_dados[0].head(10)) #  Criou uma lista de tabelas, por isso o [0]