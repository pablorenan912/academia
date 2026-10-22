from django.urls import path

from . import views

app_name = "gym"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("alunos/", views.AlunoListView.as_view(), name="aluno_list"),
    path("alunos/novo/", views.AlunoCreateView.as_view(), name="aluno_create"),
    path("alunos/<str:pk>/", views.AlunoDetailView.as_view(), name="aluno_detail"),
    path("alunos/<str:pk>/editar/", views.AlunoUpdateView.as_view(), name="aluno_update"),
    path("planos/", views.PlanoListView.as_view(), name="plano_list"),
    path("planos/novo/", views.PlanoCreateView.as_view(), name="plano_create"),
    path("planos/<str:pk>/editar/", views.PlanoUpdateView.as_view(), name="plano_update"),
    path("pagamentos/", views.PagamentoListView.as_view(), name="pagamento_list"),
    path("pagamentos/novo/", views.PagamentoCreateView.as_view(), name="pagamento_create"),
    path("frequencias/", views.FrequenciaListView.as_view(), name="frequencia_list"),
]
