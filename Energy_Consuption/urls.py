
from django.contrib import admin
from django.urls import path, include
from audit import urls
from Machine_usage import urls

urlpatterns = [
    path('energy/',include('audit.urls')),
    path('',include('Machine_usage.urls')),
    path('admin/', admin.site.urls),
    path('boiler/',include('Boiler.urls')),
    path('water/',include('Water_system.urls')),
]
