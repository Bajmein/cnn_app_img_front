from django.http import HttpResponse
from django.shortcuts import render
import requests


def clasificador_imagenes(request) -> HttpResponse:
    resultado = None

    if request.method == 'POST' and request.FILES.get('imagen'):
        imagen = request.FILES['imagen']

        api_url: str = "http://127.0.0.1:8080/predict/"

        try:
            files: dict = {"file": (imagen.name, imagen.read(), imagen.content_type)}
            response: requests.Response = requests.post(api_url, files=files)

            if response.status_code == 200:
                resultado = response.json().get('prediction', 'Sin resultado')
            else:
                resultado = f"Error: {response.json().get('detail', 'Desconocido')}"

        except requests.exceptions.RequestException as e:
            resultado = f"Error al conectar con la API: {str(e)}"

    return render(request, 'clasificador.html', {'resultado': resultado})
