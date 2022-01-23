from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro_Depoimento/', views.cadastro_Depoimento, name='cadastro_Depoimento'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('vagas_aberta/', views.vagas_aberta, name='vagas_aberta'),
    path('vagas_favoritas/', views.vagas_favoritas, name='vagas_favoritas'),
    path('perfil_jovem/', views.perfil_jovem, name='perfil_jovem'),
    path('alterar_perfil/', views.alterar_perfil, name='alterar_perfil'),
    path('empresasfavoritas/', views.empresasfavoritas, name='empresasfavoritas'),
    path('dicasjovem/', views.dicasjovem, name='dicasjovem'),
    path('candidato<int:pk>/',views.candidato, name='candidato'),

]
