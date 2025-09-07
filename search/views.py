from django.shortcuts import render
from apps.models import App

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = App.objects.filter(title__icontains=query)  # Поиск по имени
    return render(request, 'search.html', {'results': results, 'query': query})