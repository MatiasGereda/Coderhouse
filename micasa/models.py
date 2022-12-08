from django.db import models
from django.utils import timezone

# Create your models here.

class Familiar(models.Model): 
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    fecha= models.DateField(timezone.now)
    