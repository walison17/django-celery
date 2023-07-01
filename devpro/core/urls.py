from django.urls import path

from devpro.core.views import nova_proposta

app_name = "core"
urlpatterns = [
    path("propostas", nova_proposta),
]
