from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'filamento/dashboard.html')


@login_required
def fila(request):
    return render(request, 'filamento/filadeimpressao.html')


@login_required
def vender(request):
    return render(request, 'filamento/vender.html')


@login_required
def concluido(request):
    return render(request, 'filamento/concluidos.html')