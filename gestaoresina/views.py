from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
	return render(request, "resina/dashboard.html")


@login_required
def fila(request):
	return render(request, "resina/filadeimpressao.html")


@login_required
def vender(request):
	return render(request, "resina/vender.html")


@login_required
def concluido(request):
	return render(request, "resina/concluidos.html")
