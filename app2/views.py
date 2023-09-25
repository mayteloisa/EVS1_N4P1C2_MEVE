from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("<h1 style color:black> estoy en la rama 2 y en la app2</h1>")

def pregunta(request):
    return HttpResponse("<h4 style color:black>¿cómo estan en la app2?</h4>")