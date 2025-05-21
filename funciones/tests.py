from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from urllib.parse import urlencode

class ConsultarRestaurantesJWTTest(APITestCase):
    def setUp(self):
        
        self.username = "testuser"
        self.password = "Aa123456"
        self.user = User.objects.create_user(username=self.username, password=self.password)

       
        response = self.client.post("/api/usuarios/login/", {
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(response.status_code, 200)
        self.token = response.data["access"]
        
        base_url = reverse("restaurantes-list")
        params = {"ciudad": "Duitama"}
        self.url = f"{base_url}?{urlencode(params)}"

    def test_consultar_restaurantes_autenticado(self):
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

       
        response = self.client.get(self.url)
      
        self.assertEqual(response.status_code, 200)
        self.assertIn("lista_restaurantes", response.json())

    def test_consultar_restaurantes_sin_autenticacion(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)  

    def test_consultar_restaurantes_token_mal(self):
        
        self.client.credentials(HTTP_AUTHORIZATION="Bearer Caloososos1254")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)