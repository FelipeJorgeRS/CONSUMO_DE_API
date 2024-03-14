import requests
import xml.etree.ElementTree as ET

url = 'https://viacep.com.br/ws/'
cep = 30140071
formato = '/xml/'

r = requests.get(url + str(cep) + formato)

if (r.status_code == 200):
        # Converte a resposta JSON para XML como o método nativo
        root = ET.fromstring(r.content)
        xml_string = ET.tostring(root, encoding='utf-8', method='xml')

        print()
        print('XML : ', xml_string.decode())
else:
        print("Não houve sucesso na requisição. Erro:" + r.status_code)