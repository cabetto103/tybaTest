from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import RegistroLogsRestaurantes
from .serializador import LogEntrySerializerRest
    
class LogListViewRest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs_rest = RegistroLogsRestaurantes.objects.filter(usuario=request.user).order_by('-fecharegistro')
        serializer = LogEntrySerializerRest(logs_rest, many=True)
        return Response(serializer.data)