from django.urls import path

from . import views


app_name = "resina"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("fila/", views.fila, name="fila"),
    path("vender/", views.vender, name="vender"),
    path("concluido/", views.concluido, name="concluido"),
]