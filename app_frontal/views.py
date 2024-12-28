from django.http import HttpResponse
from django.shortcuts import render
import time
import requests


def home(request):
    return render(request, 'home.html')
def clasificador_imagenes(request) -> HttpResponse:
    resultado = None
    tiempo_total: None | float = None

    if request.method == 'POST' and request.FILES.get('imagen'):
        imagen = request.FILES['imagen']

        # api_url: str = "http://ec2-184-72-76-118.compute-1.amazonaws.com:8080/predict/"
        api_url: str = "http://127.0.0.1:8080/predict/"

        try:
            files: dict = {"file": (imagen.name, imagen.read(), imagen.content_type)}
            tiempo_inicio: float = time.time()
            response: requests.Response = requests.post(api_url, files=files)

            if response.status_code == 200:
                resultado = response.json().get('prediction', 'Sin resultado')
                tiempo_fin: float = time.time()
                tiempo_total: float = round(tiempo_fin - tiempo_inicio, 2)
            else:
                resultado = f"Error: {response.json().get('detail', 'Desconocido')}"

        except requests.exceptions.RequestException as e:
            resultado = f"Error al conectar con la API: {str(e)}"

    return render(
        request,
        'clasificador.html',
        {'resultado': resultado, 'tiempo_total': tiempo_total}
    )
