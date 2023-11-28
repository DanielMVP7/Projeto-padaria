from django import forms
from .models import Cliente, Produto, Info

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = "__all__"