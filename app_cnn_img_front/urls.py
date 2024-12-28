from django.urls import path
from app_frontal.views import clasificador_imagenes, home

urlpatterns: list = [
    path('', home, name='home'),
    path('clasificador/', clasificador_imagenes, name='clasificador'),
]