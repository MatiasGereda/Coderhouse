from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.template import Template, context
from .models import Familiar

# Create your views here.


def pagina (request):
    familiar1=Familiar("Gabriel",28,1994/9/19)
    familiar2=Familiar("Daniel",42,1980/1/13)
    familiar3=Familiar("German",38,1984/5/25)

    archivo=open("C:/Users/Matias/Desktop/Entorno1/virtual/MVTMatias/Templates/template1.html")

    template=Template(archivo.read)

    archivo.close()
    contexto=context(familiar1)
    contexto1=context(familiar2)
    contexto2=context(familiar3)
    documento=template.render(contexto,contexto1,contexto2)
    return HttpResponse(documento)
    
    