from django.db import models

class Cotacao(models.Model):
    uasg = models.TextField()
    numero = models.TextField()
    objeto = models.TextField()
    link = models.TextField()
    data_abertura = models.TextField()
    observacoes = models.TextField()
    situacao = models.TextField()
    data_encerramento = models.TextField()
    hora_encerramento = models.TextField()
    valor_maximo = models.TextField()
    exibir = models.BooleanField()

    def __str__(self):
        return self.numero + ' ' + self.objeto

#classe para gravar os links da paginia principal das cotacoes
class ListaPP(models.Model):
    linkpp = models.TextField()

    def __str__(self):
        return self.linkpp
