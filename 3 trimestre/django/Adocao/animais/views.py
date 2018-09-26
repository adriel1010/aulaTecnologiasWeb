# uma classe simples para exibir uma página simples
from django.views.generic import TemplateView
#serve para páginas q só tem html, talvez alguma consulta para listar alguma coisa do banco.

# página inicial
class Index(TemplateView):
    template_name = "pagina_inicial.html"

# página de ajuda
class Ajuda(TemplateView):
        template_name = "ajuda.html"
