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

    def __str__(self):
        return self.numero + ' ' + self.objeto
