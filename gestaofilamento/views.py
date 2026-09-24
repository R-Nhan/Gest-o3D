from decimal import Decimal, InvalidOperation

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import VendaForm
from .models import Venda


@login_required
def dashboard(request):
    return render(request, 'filamento/dashboard.html')


@login_required
def fila(request):
    if request.method == 'POST':
        venda_id = request.POST.get('venda_id')
        action = request.POST.get('action', 'executar')

        if action == 'excluir':
            Venda.objects.filter(id=venda_id).delete()
        elif action == 'pronto':
            Venda.objects.filter(id=venda_id, fila='executando').update(fila='pronto')
        else:
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
            messages.success(request, 'Venda registrada com sucesso.')
            return redirect('vender')
    else:
        form = VendaForm()

    return render(request, 'filamento/vender.html', {'form': form})


@login_required
def concluido(request):
    if request.method == 'POST':
        venda_id = request.POST.get('venda_id')
        action = request.POST.get('action')

        if action == 'excluir':
            Venda.objects.filter(
                id=venda_id,
                fila__in=['pronto', 'entregue'],
            ).delete()
        elif action == 'entregar':
            try:
                valor = Decimal(request.POST.get('valor', '').replace(',', '.'))
            except (AttributeError, InvalidOperation):
                messages.error(request, 'Informe valores financeiros válidos para entregar o pedido.')
                return redirect('concluido')

            venda = Venda.objects.filter(id=venda_id, fila='pronto').first()
            if venda:
                custo = venda.custo
                lucro = valor - custo
                lucro_percentual = (lucro / custo * Decimal('100')) if custo else Decimal('0')
                venda.pagamento = request.POST.get('pagamento', 'pendente')
                venda.valor = valor
                venda.lucro = lucro
                venda.lucro_percentual = lucro_percentual
                venda.status = 'pago' if venda.pagamento != 'pendente' else 'aberto'
                venda.fila = 'entregue'
                venda.save(update_fields=[
                    'pagamento', 'valor', 'lucro', 'lucro_percentual',
                    'status', 'fila',
                ])

        return redirect('concluido')

    vendas_concluidas = Venda.objects.filter(fila='pronto').order_by('-data')
    vendas_entregues = Venda.objects.filter(fila='entregue').order_by('-data')

    return render(request, 'filamento/concluidos.html', {
        'vendas_concluidas': vendas_concluidas,
        'vendas_entregues': vendas_entregues,
    })