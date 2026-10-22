from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Aluno, Pagamento, PlanoDeTreino


class StyledAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "autofocus": True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "cpf", "email", "telefone", "data_nascimento", "plano", "ativo"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "data_nascimento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "plano": forms.Select(attrs={"class": "form-select"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class PlanoDeTreinoForm(forms.ModelForm):
    class Meta:
        model = PlanoDeTreino
        fields = ["nome", "descricao", "valor_mensal", "duracao_dias"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "valor_mensal": forms.NumberInput(attrs={"class": "form-control"}),
            "duracao_dias": forms.NumberInput(attrs={"class": "form-control"}),
        }


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ["aluno", "valor", "data_pagamento", "referente_a", "forma_pagamento"]
        widgets = {
            "aluno": forms.Select(attrs={"class": "form-select"}),
            "valor": forms.NumberInput(attrs={"class": "form-control"}),
            "data_pagamento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "referente_a": forms.TextInput(attrs={"class": "form-control"}),
            "forma_pagamento": forms.Select(attrs={"class": "form-select"}),
        }
