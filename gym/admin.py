from django.contrib import admin

from .models import Aluno, Frequencia, Pagamento, PlanoDeTreino


@admin.register(PlanoDeTreino)
class PlanoDeTreinoAdmin(admin.ModelAdmin):
    list_display = ("nome", "valor_mensal", "duracao_dias")


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "plano", "ativo", "data_cadastro")
    list_filter = ("ativo", "plano")
    search_fields = ("nome", "cpf", "email")


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ("aluno", "valor", "data_pagamento", "forma_pagamento")
    list_filter = ("forma_pagamento",)


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ("aluno", "data", "presente")
    list_filter = ("presente",)
