from django.db import models


class Proposta(models.Model):
    nome_completo = models.CharField(max_length=256)
    cpf = models.CharField(max_length=16)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    aprovada = models.BooleanField(default=False)

    def as_dict(self):
        return {
            "id": self.pk,
            "nome_completo": self.nome_completo,
            "cpf": self.cpf,
            "valor": self.valor,
            "aprovada": self.aprovada
        }
