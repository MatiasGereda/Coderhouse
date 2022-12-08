from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.template import Template, Context
from .models import Familiar

# Create your views here.


def Familiar (request):
    familiar1=Familiar(nombre="Gabriel", edad=28)
    familiar2=Familiar(nombre="Daniel", edad=42)
    familiar3=Familiar(nombre="German", edad=38)
    


    archivo=open("C:/Users/Matias/Desktop/Entorno1/Nueva/Coderhouse/Templates/template1.html")

    template=Template(archivo.read())

    archivo.close()
   
    documento=template.render()
    return HttpResponse(documento)
    
    