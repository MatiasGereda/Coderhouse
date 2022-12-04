from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

# Create your views here.


def familiar(request):
    familiar1=Familiar(nombre="Gabriel", edad=28, nacimiento=1994)
    familiar2=Familiar(nombre="Julia", edad=58, nacimiento=1964)
    familiar3=Familiar(nombre="Daniel", edad=40, nacimiento=1982)
    familiar1.save()
    familiar2.save()
    familiar3.save()
    texto=f"hola, me llamo Matias y vivo con mi hermano que se llama {familiar1.nombre}, tiene {familiar1.edad} años y nacio en el {familiar1.nacimiento}, tengo otro hermano que se llama {familiar3.nombre}, tiene {familiar3.edad} y nacio en el {familiar3.nacimiento}. Soy hijo de {familiar2.nombre} la cual tiene {familiar2.edad} ya que nacio en {familiar2.nacimiento}."
    return HttpResponse(texto)