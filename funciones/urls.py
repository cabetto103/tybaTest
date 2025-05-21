from django.urls import path
from .views import ListaRestaurantesView


urlpatterns = [    
    path('consultar_restaurantes/', ListaRestaurantesView.as_view(), name='restaurantes-list-detail'),
]
