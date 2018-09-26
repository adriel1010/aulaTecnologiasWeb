from django.urls import path
#importa tudo q tem la na view.py do app "animais"
from .views import *
# o ponto indica par ao python buscar o views dentro deste diretório
# * indica q ta importando tudo.



urlpatterns = [
    # passa o endereço e o método la da view q irá processar esse endereço
    path('', Index.as_view(), name="index" ),
    path('ajuda/', Ajuda.as_view(), name="ajuda"),
]
