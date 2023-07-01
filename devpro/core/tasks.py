import random
import time
from celery import shared_task

from devpro.core.models import Proposta


@shared_task
def analisar_proposta(proposta_id):
    time.sleep(10)
    proposta = Proposta.objects.get(id=proposta_id)
    proposta.aprovada = algoritmo_analise()
    proposta.save(update_fields=["aprovada"])
    return proposta.aprovada


def algoritmo_analise():
    return random.random() > 0.5
