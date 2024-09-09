from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)  # Cambiado a CharField para el nombre
    description = models.TextField(null=True, blank=True)  # Descripción opcional y larga
    fecha_escogida = models.DateTimeField(default=timezone.now)  # Fecha y hora actuales por defecto
    fecha_limite = models.DateTimeField(default=timezone.now)  # Fecha y hora actuales por defecto
    nivel = models.FloatField(null=True, blank=True)  # Valor numérico opcional
    etiqueta = models.CharField(max_length=200, null=True, blank=True)  # Usar CharField para etiquetas si es solo texto




    