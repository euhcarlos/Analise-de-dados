import requests

from coleta_dados_web import requisition


def enviar_arquivo():
    #  Caminho do arquivo para upload
    caminho = 'C:/Users/dudu/Downloads/produtos_informatica.xlsx'

    #  Enviar o arquivo
    requisition = requests.post('https://file.io', files={'file':open(caminho, 'rb')})
    saida_requisition = requisition.json()

    print(saida_requisition)
    url = saida_requisition['link']
    print("Arquivo enviado. Link para acesso", url)

def enviar_arquivo_chave():
    # Caminho do arquivo para upload com chave
    caminho = 'C:/Users/dudu/Downloads/produtos_informatica.xlsx'
    api_key = 'INJBQQJ.8131GG2-G9X4PAT-PQBTSJR-1MS4P00'

    #  Enviar o arquivo
    requisition = requests.post(
        'https://file.io',
        files={'file':open(caminho, 'rb')},
        headers={'Authorization':api_key}
    )

    saida_requisition = requisition.json()

    print(saida_requisition)
    url = saida_requisition['link']
    print("Arquivo enviado. Link para acesso", url)

def receber_arquivo(file_url):
    #  Receber arquivo
    requisition = requests.get(file_url)

    #  Salvar o arquivo
    if requisition.ok:
        with open('arquivo_baixo.xlsx', 'wb') as file:
            file.write(requisition.content)
            print('Arquivo baixado com sucesso')
    else:
        print('Erro ao baixa o arquivo:', requisition.json())

#  enviar_arquivo()
#  enviar_arquivo_chave()
receber_arquivo('https://file.io/T7rfs8fZvU1N')