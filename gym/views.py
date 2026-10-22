from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .forms import AlunoForm, PagamentoForm, PlanoDeTreinoForm
from .models import Aluno, Frequencia, Pagamento, PlanoDeTreino


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "gym/dashboard.html"


# Alunos (RF001 - cadastrar, RF005 - consultar)

class AlunoListView(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = "gym/aluno_list.html"
    context_object_name = "alunos"
    ordering = ["nome"]


class AlunoDetailView(LoginRequiredMixin, DetailView):
    model = Aluno
    template_name = "gym/aluno_detail.html"
    context_object_name = "aluno"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagamentos"] = self.object.pagamentos.all()
        context["frequencias"] = self.object.frequencias.all()
        return context


class AlunoCreateView(LoginRequiredMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "gym/aluno_form.html"
    success_url = reverse_lazy("gym:aluno_list")


class AlunoUpdateView(LoginRequiredMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "gym/aluno_form.html"
    success_url = reverse_lazy("gym:aluno_list")


# Planos de treino (RF002)

class PlanoListView(LoginRequiredMixin, ListView):
    model = PlanoDeTreino
    template_name = "gym/plano_list.html"
    context_object_name = "planos"
    ordering = ["nome"]


class PlanoCreateView(LoginRequiredMixin, CreateView):
    model = PlanoDeTreino
    form_class = PlanoDeTreinoForm
    template_name = "gym/plano_form.html"
    success_url = reverse_lazy("gym:plano_list")


class PlanoUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanoDeTreino
    form_class = PlanoDeTreinoForm
    template_name = "gym/plano_form.html"
    success_url = reverse_lazy("gym:plano_list")


# Pagamentos (RF003)

class PagamentoListView(LoginRequiredMixin, ListView):
    model = Pagamento
    template_name = "gym/pagamento_list.html"
    context_object_name = "pagamentos"


class PagamentoCreateView(LoginRequiredMixin, CreateView):
    model = Pagamento
    form_class = PagamentoForm
    template_name = "gym/pagamento_form.html"
    success_url = reverse_lazy("gym:pagamento_list")


# Frequência (RF004) - listagem somente leitura nesta entrega

class FrequenciaListView(LoginRequiredMixin, ListView):
    model = Frequencia
    template_name = "gym/frequencia_list.html"
    context_object_name = "frequencias"
