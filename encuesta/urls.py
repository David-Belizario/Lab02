from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar/', views.enviar, name='enviar'),
    path('calcular/', views.calcular, name='calcular'),
    path('volumen_cilindro/', views.volumen_cilindro, name='volumen_cilindro'),
]
