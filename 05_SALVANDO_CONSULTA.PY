import requests
r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})

if (r.status_code == 200):
          print()
         # print('Retorno : ', r.text)
          #salvando a consulta em um arquivo
          with open('result_consulta.txt','a') as arquivo :
                  arquivo.write(r.text)
          print("A consulta foi gravada no arquivo com sucesso")
else:
          print('Nao houve sucesso na requisicao.')