from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaUno(request):
    html="""
    <h1 style="color:blue"> holaaaaaa mundito </h1>
    <h2 style="color:blue"> holaaaaaa munditotitoooooo </h2>
    <h3 style="color:blue"> holaaaaaa mundito holiwissss </h3>
    <h4 style="color:blue"> holaaaaaa mundito holissssss </h4>
    """
    return HttpResponse(html)

def vistaDos (request):
    vista2="""
    <h4 style="color:red"> viva la programación </h4>
    <h1 style="color:red"> viva la vida </h1>
    <h3 style="color:red"> viva la fiesta </h3>
    <h4 style="color:red"> viva la wtf?</h4>
    """
    return HttpResponse(vista2)