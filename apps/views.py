from django.shortcuts import render
from apps.models import App
from django.shortcuts import render, get_object_or_404

# Create your views here.
def apps(request):
    apps = App.objects.order_by('-id')
    data = {
        'apps': apps,
    }
    return render(request, 'app_info.html', context=data)

def app_case(request, id):
    get_object_or_404(App, id=id)
    app_case = App.objects.filter(id=id)
    data = {
        'app_case': app_case,
    }
    return render(request, 'app_info.html', data)