from django.urls import path
from app_frontal.views import clasificador_imagenes

urlpatterns = [
    path('', clasificador_imagenes, name='clasificador'),
]