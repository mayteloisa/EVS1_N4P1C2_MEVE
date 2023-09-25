from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("<h1 style color:black> estoy en la rama 2 y en la app2</h1> <h2 style color:red>Espero sacarme buena nota</h2><h3 style color:black> no se que mas escribir</h3><h4 style color:black>fin</h4> ")

def pregunta(request):
    return HttpResponse("<h4 style color:black>¿cómo estan en la app2?</h4><h5 style color:black>vista 2</h5><h3 style color:black>ya no se que poner</h3><h2 style color:black>fin vista2</h2>")