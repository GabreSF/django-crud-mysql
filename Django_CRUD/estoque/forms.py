# SeuApp/forms.py
from django import forms
from .models import Produto

class PlaceholderTextarea(forms.Textarea):
    def __init__(self, placeholder_text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['placeholder'] = placeholder_text

class ProdutoForm(forms.ModelForm):
    descricao = forms.CharField(
        label='',  # Defina o rótulo como uma string vazia
        widget=PlaceholderTextarea("Insira a descrição do produto aqui..."),
        max_length=200,
    )

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

