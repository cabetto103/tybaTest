from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import RegistroLogsRestaurantes
from .serializador import LogEntrySerializerRest
    
class LogListViewRest(APIView):
    """
    API endpoint para consultar en log de consultas realizadas por usuario.

    GET:
        Consulta el registro log de las consultas realizadas al endpoint consultar restaurantes 
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Consulta el historial de consultas realizadas por el usuario.

        Args:
            request (HttpRequest): Solicitud HTTP GET con validacion de autorizacion y parametro ciudad o latitud y longitud.

        Returns:
            Response: Codigos de status HTTP 201, o errores con status HTTP 400, informacion con los registros log serializada.
        """     
        logs_rest = RegistroLogsRestaurantes.objects.filter(usuario=request.user).order_by('-fecharegistro')
        serializer = LogEntrySerializerRest(logs_rest, many=True)
        return Response(serializer.data)