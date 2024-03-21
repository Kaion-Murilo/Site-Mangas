from django.shortcuts import render
import requests  # Importe o objeto request

# Seu código de visualização continua aqui...


def index(request):
    print('passouo aqui')
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        return search_manga(query)
    return render(request, 'search.html')

import requests

def search_manga(query):
    # Realiza a pesquisa de mangás na API do MangaDex
    API_BASE_URL = "https://api.mangadex.org"
    endpoint = f"{API_BASE_URL}/manga?title={query}"
    
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        
        if response.status_code == 200:
            data = response.json()
            mangas = data['data']
            mangas = {'mangas': mangas}
            return render(request, 'results.html', mangas)
        else:
            return render(request, 'error.html')
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer solicitação: {e}")
        return render(request, 'error.html')
