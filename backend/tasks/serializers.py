from rest_framework import serializers
from .models import Tarea
#Las apirest full permiten el intercambio de información de manera segura a traves de internet , rest es una arquitectura de software que impone condiciones sobre como debe funcionar una API 
#La serialización consiste en un proceso de codificación de un objeto es una representación con toda la información necesaria para crear una nueva instancia del objeto que es idéntica en todo al original 


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = [
            'nombre',
            'descripcion',
            'fecha_escogida',
            'fecha_limite',
            'nivel',
            'etiqueta'
        ]
        

