import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Proposta
from .tasks import analisar_proposta


@csrf_exempt
def nova_proposta(request):
    data = json.loads(request.body)

    proposta = Proposta.objects.create(
        nome_completo=data["nome_completo"],
        cpf=data["cpf"],
        valor=data["valor"],
    )
    analisar_proposta.delay(proposta.pk)

    return JsonResponse(proposta.as_dict(), status=201)
