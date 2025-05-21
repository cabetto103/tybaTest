from rest_framework import serializers
from .models import RegistroLogsRestaurantes

class LogEntrySerializerRest(serializers.ModelSerializer):
    class Meta:
        model = RegistroLogsRestaurantes
        fields = '__all__'
        read_only_fields = ['id', 'fecharegistro']