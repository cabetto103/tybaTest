# tasks/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from logs.util import crear_log_restaurantes
# from django.shortcuts import render
import requests

class ListaRestaurantesView(APIView):
    """
    API endpoint para consultar los restaurantes cercanos en una ciudad
    o coordendas especificas.

    GET:
        Consulta Un servicio externo que nos restorna infomacion de restaurantes
    """
    permission_classes = [IsAuthenticated]
    def get(self, request): 
        """
        Consulta los restaurantes disponibles

        Args:
            request (HttpRequest): Solicitud HTTP POST con validacion de autorizacion.

        Returns:
            Response: Codigos de status HTTP 201, o errores con status HTTP 400 y un listado de restaurantes
        """     
        try:
            ciudad = request.query_params.get('ciudad')
            lat = request.query_params.get('latitud')
            lon = request.query_params.get('longitud')
            tipo_accion = "COORDENADAS"
            if ciudad:
                tipo_accion = "CIUDAD"
                # nominatim_url = f"https://nominatim.openstreetmap.org/search?city={ciudad}&format=json"
                url = f"https://nominatim.openstreetmap.org/search?city={ciudad}&format=json"
                headers = {
                    "User-Agent": "mi-app/1.0 (correo@ejemplo.com)"
                }
                resp = requests.get(url, headers=headers).json()
                # print("Status code:", resp.status_code)
                # print(resp.text)
                # print(resp.json())
                if not resp:
                    return Response({"error": "Ciudad no encontrada"}, status=400)
                lat = resp[0]['lat']
                lon = resp[0]['lon']

            if not lat or not lon:
                return Response({"error": "Debes enviar una ciudad o coordenadas válidas"}, status=400)

            overpass_url = "http://overpass-api.de/api/interpreter"
            query = f"""
            [out:json];
            (
            node["amenity"="restaurant"](around:2000,{lat},{lon});
            );
            out;
            """
            response = requests.post(overpass_url, data={"data": query})
            data = response.json()

            restaurantes = []
            for element in data.get("elements", []):
                nombre = element.get("tags", {}).get("name", "Sin nombre")
                direccion = element.get("tags", {}).get("addr:full", "Desconocida")
                restaurantes.append({
                    "nombre": nombre,
                    # "direccion": direccion,
                    "lat": element.get("lat"),
                    "lon": element.get("lon")
                })           
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        crear_log_restaurantes(request.user, tipo_accion, {"Ciudad":ciudad,"latitud":lat,"longitud":lon} ,{"restaurantes":restaurantes})
        return Response({"lista_restaurantes": restaurantes}, status=status.HTTP_200_OK)
    
