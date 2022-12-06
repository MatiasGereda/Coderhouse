from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.template import Template, Context
from .models import Familiar

# Create your views here.


def pagina (request):
    familiar1=Familiar("Gabriel",28)
    familiar2=Familiar("Daniel",42)
    familiar3=Familiar("German",38)

    archivo=open("C:/Users/Matias/Desktop/Entorno1/Nueva/Coderhouse/Templates/template1.html")

    template=Template(archivo.read())

    archivo.close()
    contexto=Context(familiar1)
    contexto1=Context(familiar2)
    contexto2=Context(familiar3)
    documento=template.render(contexto1)
    return HttpResponse(documento)
    
    