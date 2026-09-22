from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import VendaForm


@login_required
def dashboard(request):
    return render(request, 'filamento/dashboard.html')


@login_required
def fila(request):
    return render(request, 'filamento/filadeimpressao.html')


@login_required
def vender(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vender')
    else:
        form = VendaForm()

    return render(request, 'filamento/vender.html', {'form': form})


@login_required
def concluido(request):
    return render(request, 'filamento/concluidos.html')