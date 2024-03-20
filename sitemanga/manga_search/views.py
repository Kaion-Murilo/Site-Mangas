from django.shortcuts import render
import requests

def index(request):
    return render(request,'index.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        return search_manga(query)
    return render(request, 'search.html')

def search_manga(query):
    # Realiza a pesquisa de mangás na API do MangaDex
    API_BASE_URL = "https://api.mangadex.org"
    endpoint = f"{API_BASE_URL}/manga?title={query}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        mangas = data['data']
        return render(request, 'results.html', {'mangas': mangas})
    else:
        return render(request, 'error.html')

