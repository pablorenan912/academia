from django.db import models


class PlanoDeTreino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    valor_mensal = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_dias = models.PositiveIntegerField(help_text="Duração do plano em dias")

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    plano = models.ForeignKey(
        PlanoDeTreino, on_delete=models.SET_NULL, null=True, blank=True, related_name="alunos"
    )
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pagamento(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ("dinheiro", "Dinheiro"),
        ("cartao", "Cartão"),
        ("pix", "Pix"),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="pagamentos")
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_pagamento = models.DateField()
    referente_a = models.CharField(max_length=100, help_text="Ex: Mensalidade Maio/2026")
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO_CHOICES, default="dinheiro")

    def __str__(self):
        return f"{self.aluno.nome} - {self.referente_a}"

    class Meta:
        ordering = ["-data_pagamento"]


class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="frequencias")
    data = models.DateField()
    horario = models.DateTimeField(auto_now_add=True)
    presente = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.data}"

    class Meta:
        ordering = ["-data", "-horario"]
