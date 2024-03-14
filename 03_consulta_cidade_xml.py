import requests
import xml.etree.ElementTree as ET

def consulta_endereco(estado, cidade, rua):
    url = 'https://viacep.com.br/ws/'
    formato = '/xml/'

    r = requests.get(url + estado + '/' + cidade + '/' + rua + formato)

    if (r.status_code == 200):
        # Converte a resposta XML para uma string
        root = ET.fromstring(r.content)
        xml_string = ET.tostring(root, encoding='utf-8', method='xml')
        print()
        print('XML : ', xml_string.decode())

estado = 'MG'  
cidade = 'Belo Horizonte'  
rua = 'Rua Rio de Janeiro'

consulta_endereco(estado, cidade, rua)
