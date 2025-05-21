from django.urls import path
from .views import LogListViewRest

urlpatterns = [
    # path('', LogListView.as_view(), name='log-list'),
    path('logs_consultas_restaurantes/', LogListViewRest.as_view(), name='logs-restaurantes'),
]
