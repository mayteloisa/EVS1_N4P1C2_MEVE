from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaUno(request):
    html="""
    <h1 style="color:blue"> holaaaaaa mundito </h1>
    """
    return HttpResponse(html)

def vistaDos (request):
    vista2="""
    <h4 style="color:red"> viva la programación </h4>
    """
    return HttpResponse(vista2)