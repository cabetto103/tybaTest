from django.db import models
from django.contrib.auth.models import User

class RegistroLogsRestaurantes(models.Model):
    ACTION_CHOICES = [
        ('CIUDAD', 'Ciudad'),
        ('COORDENADAS', 'Coordendas'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='user_logs')
    accion = models.CharField(max_length=20, choices=ACTION_CHOICES)
    fecharegistro= models.DateTimeField(auto_now_add=True)
    metadatain = models.JSONField(default=dict)
    metadataout = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.fecharegistro} - {self.usuario} - {self.accion}"

