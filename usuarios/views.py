
from django.shortcuts import render
from rest_framework import generics,status
from .serializador import RegisterSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

       
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"error": "No refresh token provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Verificar que el refresh token pertenece al usuario autenticado
            payload = jwt_decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
            token_user_id = payload.get("user_id")

            if token_user_id != request.user.id:
                return Response({"error": "No tienes permiso para cerrar esta sesión."}, status=status.HTTP_403_FORBIDDEN)

            # Invalidar (blacklist) el token
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Sesión cerrada correctamente."}, status=status.HTTP_205_RESET_CONTENT)

        except TokenError:
            return Response({"error": "Token inválido o ya fue revocado."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "Error procesando el token."}, status=status.HTTP_400_BAD_REQUEST)
