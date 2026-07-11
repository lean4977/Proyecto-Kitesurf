from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('instructor/', views.instructor, name='perfil_instructor'),
    path('materiales/', views.equipamiento, name='materiales'),
    path('cursos-precios/', views.cursos_precios, name='cursos_precios'), 
    path('registro/', views.registro, name='registro'),
    path('reservar/', views.reservar, name='reservar'),
]