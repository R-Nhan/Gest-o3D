from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import VendaForm
from .models import Venda


@login_required
def dashboard(request):
    return render(request, 'filamento/dashboard.html')


@login_required
def fila(request):
    if request.method == 'POST':
        venda_id = request.POST.get('venda_id')
        Venda.objects.filter(id=venda_id, fila='espera').update(fila='executando')
        return redirect('fila')

    vendas_executando = Venda.objects.filter(fila='executando').order_by('data')
    vendas_em_espera = Venda.objects.filter(fila='espera').order_by('data')

    return render(request, 'filamento/filadeimpressao.html', {
        'vendas_executando': vendas_executando,
        'vendas_em_espera': vendas_em_espera,
    })


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