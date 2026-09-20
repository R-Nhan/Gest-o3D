
from django.urls import path, include
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("fila/", views.fila, name="fila"),
    path("vender/", views.vender, name="vender"),
    path("concluido/", views.concluido, name="concluido"),
]