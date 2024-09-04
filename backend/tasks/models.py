from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre= models.TextField(max_length=200)
    description=models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)




    