from django.urls import path
from apps.views import apps, app_case

urlpatterns = [
    path('', apps, name='apps'),
    path('<int:id>/', app_case, name='app_case'),
    #path('admin/', admin.site.urls),
]