from .models import RegistroLogsRestaurantes


def crear_log_restaurantes(user, action, metain=None,metaout=None):
    RegistroLogsRestaurantes.objects.create(
        usuario=user,
        accion=action,       
        metadatain=metain or {},
        metadataout=metaout or {}
    )