from django.contrib import admin
from django.urls import path

#se importan las vistas
from .views import *


urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GAL'),
    path('quienes/',quienes,name="QUIEN"),
    path('ubicacion/',ubicacion,name='UBI'),
    path('registrarse/',registrarse,name="REGIS"),
    path('ingresar/',ingresar,name="INGRE"),
    path('formulario/', formulario,name="FORMU"),
    path('login_acceso/',login_acceso, name="LOGINACCESO"),
    path('cerrar_sesion/',cerrar_sesion, name="CERRARSESION"),
    path('carritoregistrado/',carritoregistrado,name='CARRO2'),   
    path('carrito/',carrito,name="CARRITO"),
    path('carro_compras/<id>',carro_compras,name='AGREGAR_CARRO'),
    path('carro_mas/<id>/', carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<id>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name="GRABAR_CARRO"),
    path('vacir_carrito/',vacio_carrito,name='VACIARCARRITO'),
]
