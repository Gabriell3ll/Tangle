from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio,name="inicio"),
    path('Temperatura/',views.Temperatura,name="Temperatura"),
    path('Temperatura2/',views.Temperatura2,name="Temperatura2"),
    path('Humedad/',views.Humedad,name="Humedad"),
    path('Humedad2/',views.Humedad2,name="Humedad2"),
    path('Presion2/',views.Presion2,name="Presion2"),
    path('Presion/',views.Presion,name="Presion"),
    path('export_xls/', views.export_xls,name="export_xls"),
]