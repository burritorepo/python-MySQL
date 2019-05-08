"""ProjectoBarberia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ReservaBarberia import views
from django.contrib.auth.views  import LoginView
from rest_framework import routers

from ReservaBarberia.views import RegistrarBarbero

from ReservaBarberia.views import RegistrarCliente

from ReservaBarberia.views import barberos_listado

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('codigo/django',views.ejemplo,name='ejemplo'),
    path('inicio/',views.index,name='index'),

    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('barberos/',include('ReservaBarberia.urls',namespace='barberosapp')),
    path('django-sb-admin/', include('django_sb_admin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)