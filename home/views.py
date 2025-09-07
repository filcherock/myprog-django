from django.shortcuts import render
from apps.models import App
import os

# Create your views here.
def index(request):
    apps = App.objects.order_by('-id')
    data = {
        'apps': apps,
    }
    return render(request, 'index.html', context=data)
    