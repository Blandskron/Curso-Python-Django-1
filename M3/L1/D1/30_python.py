# Ejemplo 30: Vista muy simple en Django (función de vista)
# Este código se usa dentro de un proyecto Django real.
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django")  # Respuesta HTTP simple

# En urls.py del proyecto se podría usar:
# from django.urls import path
# from .views import saludo
#
# urlpatterns = [
#     path("saludo/", saludo),
# ]
