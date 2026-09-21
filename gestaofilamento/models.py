from django.db import models

from django.db import models


class Venda(models.Model):

    FILA_CHOICES = [
        ('espera', 'Espera'),
        ('executando', 'Executando'),
        ('pronto', 'Pronto'),
        ('entregue', 'Entregue'),
    ]

    PAGAMENTO_CHOICES = [
        ('pix', 'PIX'),
        ('dinheiro', 'Dinheiro'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('pendente', 'Pendente'),
    ]

    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ]

    id = models.AutoField(primary_key=True)

    cliente = models.CharField(max_length=150)

    produto = models.CharField(max_length=200)

    quantidade = models.PositiveIntegerField(default=1)

    link = models.URLField(blank=True, null=True)

    tamanho = models.CharField(max_length=100, blank=True, null=True)

    custo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    lucro = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    fila = models.CharField(
        max_length=20,
        choices=FILA_CHOICES,
        default='espera'
    )

    pagamento = models.CharField(
        max_length=30,
        choices=PAGAMENTO_CHOICES,
        default='pendente'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='aberto'
    )

    data = models.DateTimeField(auto_now_add=True)

    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.produto} - {self.cliente}'
