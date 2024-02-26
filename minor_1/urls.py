"""
URL configuration for minor_1 project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nofie/', include('nofie_app.urls')),
]
