import requests, csv
from bs4 import BeautifulSoup

#todo melhorar a lógica do scraping e comentar o código
# coletando a primeira página da lista de artistas

page = requests.get('http://comprasnet.gov.br/cotacao/menu.asp?filtro=livre_andamento')
soup = BeautifulSoup(page.text,'html.parser')



cotacao_list = soup.find('table')
# rows = cotacao_list.find_all('tr')


cotacao_list_items = cotacao_list.find_all('a')

pages=[]
# Criar loop para imprimir todos os nomes dos artistas
for cotacao in cotacao_list_items:
    link = 'http://comprasnet.gov.br/cotacao/' + cotacao.get('href')
    descricao = cotacao.contents[2]
    numero = cotacao.contents[1]
    pages.append(str(link))
    # print(link,numero, descricao)

i = 0
lista = []
listacotacoes = []
nin = 0
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    soup.table.b.decompose()
    detalhe_list = soup.find('b')
    detalhe_list.decompose()
    detalhe_list = soup.find('table')


    detalhe_list_item = detalhe_list.find_all('tr')
    # print(item)
    for tr in detalhe_list_item[1:]:
        lista.append(tr.find('td'))
        #
        #
        # print('#################################')
        # print(lista)
    listacotacoes.append(lista)
    lista = []

    i = i + 1
    if i == 1:
        break
print(listacotacoes)