import requests
from bs4 import BeautifulSoup

'''
Vamos iniciar o nosso projeto de extração e manipulação de dados, utilizando inicialmente os dados do e-commerce books.toscrape.com. Este é um site para fins educativos para realizar web scraping de uma página fictícia de livraria. Vamos utilizar este site pois, se utilizássemos sites de e-commerce, poderíamos ser vistos como robôs que querem tentar invadir ou derrubar o site, afinal, muitos alunos acessariam o mesmo site e realizariam consultas.

Para este primeiro exercício faça o seguinte:

- Armazene a requisição na variável extracao.
- Use o print com a requisição para chegar no resultado. Utilize também a função prettify()
- Mostre os primeiros 2000 caracteres do site https://books.toscrape.com/
'''

#  Fazendo requisição e estruturando os dados
response = requests.get('https://books.toscrape.com')
extracao = BeautifulSoup(response.text, 'html.parser')

#  Mostrando os dados
print(extracao.prettify()[:2000])

'''
Agora mostre o título e o preço dos livros da primeira página do site https://books.toscrape.com/, para fazer isso é necessário seguir os passos abaixo:

 Parte 1
  - Crie um for para encontrar a tag <h3> dentro da tag <article>
  - Extraia os textos da tag <h3> e armazene na variável titulo. Essa variável depois deve ser utilizada para atualizar o valor de livro['Título']
  - Crie outro for para encontrar a tag <p class=’’price_color’> com o findall('p', class='price_color'), dentro da tag <h3>
  - Extraia os textos da tag <p> e armazene na variável preco. Essa variável depois deve ser utilizada para atualizar o valor de livro['Preço']
  - Atente para a nomenclatura correta das variáveis e das chaves do dicionário. Os livros devem ser adicionados na lista catalogo, conforme o código padrão.
  Parte 2
  - Calcule a quantidade de livros da primeira página do site https://books.toscrape.com/:
  - Você pode utilizar a mesma estrutura de for loop feita na parte 1.
  - Armazene a quantidade de livros na variável contar_livros.
  - Imprima a variável contar_livros
'''

conta_livro = 0
catalogo = []

for article in extracao.find_all('article', class_='product_pod'):

    livro = {}

    for h in article.find_all('h3'):
        titulo = h.text.strip()
        livro['Título'] = titulo
    for p in article.find_all('p', class_='price_color'):
        preco = p.text.strip()
        livro['Preço'] = preco

    conta_livro += 1
    catalogo.append(livro)

print('Quantidade de livros: ', conta_livro)
print(catalogo)



