from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    def clean_tamanho(self):
        tamanho = self.cleaned_data.get('tamanho')
        if tamanho:
            return tamanho.strip().lower().removesuffix('cm').strip()
        return tamanho

    class Meta:
        model = Venda
        fields = [
            'cliente', 'produto', 'quantidade', 'peso', 'custo', 'valor_esperado',
            'link', 'tamanho', 'observacao'
        ]