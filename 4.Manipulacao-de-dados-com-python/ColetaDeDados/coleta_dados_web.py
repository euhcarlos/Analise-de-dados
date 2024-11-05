import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'

requisition = requests.get(url)
extract = BeautifulSoup(requisition.text, 'html.parser')

def extrairTexto():
    #  Extrair o texto
    print(extract.text.strip())

def extrairPelaTag():
    #  Filtrar exibição pela tag
    for linha_titulo in extract.find_all('h2'):
        titulo = linha_titulo.text.strip()
        print('Titulo: ', titulo)

'''
Desafio
Filtrar Tags ['h2', 'p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag)
'''

def contaTituloEParagrafo():
    ct_titulo = 0
    ct_paragrafo = 0

    for linha_texto in extract.find_all(['h2', 'p']):
        if linha_texto.name == 'h2':
            ct_titulo += 1
        elif linha_texto.name == 'p':
            ct_paragrafo += 1

    print('Quantidade títulos: ', ct_titulo)
    print('Quantidade Paragrafo: ', ct_paragrafo)

def exibirTextosDasTags():
    #  Exibir textos das tags
    for linha_texto in extract.find_all(['h2','p']):
        if linha_texto.name == 'h2':
            print('Título: \n', linha_texto.text.strip())
        elif linha_texto.name == 'p':
            print('Paragrafo: \n', linha_texto.text.strip())

def exibirTagsAninhadas():
    for titulo in extract.find_all('h2'):
        print('\n Título: ', titulo.text.strip())
        for link in titulo.find_next_sibling('p'):
            for a in link.find_all_next('a', href=True):
                print('Texto Link: ', a.text.strip(), ' |  URL: ', a['href'])



exibirTagsAninhadas()
# exibirTextosDasTags()
# extrairTexto()
# extrairPelaTag()
# contaTituloEParagrafo()
