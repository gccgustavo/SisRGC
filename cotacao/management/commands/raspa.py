from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from cotacao.models import Cotacao, ListaPP
from django.shortcuts import redirect
import requests, csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        page = requests.get('http://comprasnet.gov.br/cotacao/menu.asp?filtro=livre_andamento')
        soup = BeautifulSoup(page.text, 'html.parser')

        cotacao_list = soup.find('table')
        # rows = cotacao_list.find_all('tr')

        cotacao_list_items = cotacao_list.find_all('a')

        tt = 0
        pages = []
        pagesaux = []
        # Criar loop para imprimir todos os nomes dos artistas
        for cotacao in cotacao_list_items:
            link = 'http://comprasnet.gov.br/cotacao/' + cotacao.get('href')
            descricao = cotacao.contents[2]
            numero = cotacao.contents[1]
            # para primeira iteração do sistema em um banco novo executar essa criação
            # ListaPP.objects.create(
            #     linkpp=link
            # )
            # listaObj = ListaPP.objects.values_list()
            pagesaux.append(str(link))
            if ListaPP.objects.filter(linkpp=link).exists():
                pass
            else:
                pages.append(str(link))
                ListaPP.objects.create(
                linkpp=link
                )

            # tt = tt + 1
            # if tt == 100:
            #     break
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
            lista.append(item)
            for tr in detalhe_list_item[1:]:
                lista.append(tr.find('td'))
                #
                #
                # print('#################################')
                # print(lista)
            listacotacoes.append(lista)
            lista = []

            # i = i + 1
            # if i == 10:
            #     break

        for linha in range(0,len(listacotacoes)):
            #Tratamento dos dados para inserir no banco
            linkfinal = str(listacotacoes[linha][0])
            uasg = str(listacotacoes[linha][1]).replace('/', '').replace('<', '').replace('>', '').replace('td', '')
            numero = str(listacotacoes[linha][2]).replace('/', '').replace('<', '').replace('>', '').replace('td', '')
            objeto = str(listacotacoes[linha][3]).replace(':','').replace('Objeto','').replace('/','').replace('<','').replace('>','').replace('td','').replace('b b','')
            auxdata = str(listacotacoes[linha][4]).split(':')
            data_abertura = str(auxdata[1]).replace('</b>','').replace('</td>','')
            observacoes = str(listacotacoes[linha][5]).replace('/', '').replace('<', '').replace('>', '').replace('td', '')
            situacao = str(listacotacoes[linha][6]).replace('/', '').replace('<', '').replace('>', '').replace('td', '')

            #tratamento da data e hora de encerramento
            saida = str(listacotacoes[linha][7]).split(':')
            saida = str(saida[1]).replace('</b>', '').split(' ')
            data = saida[1]
            hora = saida[2].replace('<span', '')

            data_encerramento = data
            hora_encerramento = hora

            valorm = str(listacotacoes[linha][8]).split(':')
            valor_maximo = str(valorm[1]).replace('</b>', '').replace('.', '').replace('</td>', '')

            #inserindo no banco
            Cotacao.objects.create(
                uasg=uasg,
                numero=numero,
                objeto = objeto,
                link =linkfinal,
                data_abertura =data_abertura,
                observacoes =observacoes,
                situacao =situacao,
                data_encerramento = data_encerramento,
                hora_encerramento = hora_encerramento,
                valor_maximo = valor_maximo,
                exibir = True
            )

        # retira da exibição os itens já finalizados
        queryset_cotacao = Cotacao.objects.all()
        for mostrar in queryset_cotacao:
            if mostrar.link in pagesaux:
                pass
            else:
                mostrar.exibir = False
                mostrar.save()

        return 0