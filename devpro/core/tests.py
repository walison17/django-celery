import pytest
from unittest import mock

from decimal import Decimal


@pytest.mark.django_db
def test_criar_nova_proposta(client):
    with mock.patch("devpro.core.views.analisar_proposta") as analisar_proposta_mock:
        response = client.post(
            "/api/propostas",
            data={"nome_completo": "walison filipe", "valor": Decimal(250_000), "cpf": "99999999999"},
            content_type="application/json",
        )

    analisar_proposta_mock.delay.assert_called()
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["nome_completo"] == "walison filipe"
    assert data["cpf"] == "99999999999"
    assert data["aprovada"] is False
    assert data["valor"] == "250000"
