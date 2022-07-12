"""Evaluacion03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from app_gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingresar_persona/', views.ingresar_persona),
    path('ingreso_persona/', views.ingreso_persona),
    path('index/', views.index),
    path('listar_personas/', views.listar_personas),
    path('listar/', views.listar),
    path('busqueda_personas/', views.busqueda_personas),
    path('buscar/', views.buscar),
    path('registro_dom/', views.registro_dom),
    path('ingreso_dom/', views.ingreso_dom),
    path('listar_domicilios/', views.listar_domicilios),
    path('eliminar_personas/', views.eliminar_personas),
    path('eliminacion_personas/', views.eliminacion_personas),

]
