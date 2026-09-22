from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'produto', 'quantidade', 'link', 'tamanho', 'observacao']