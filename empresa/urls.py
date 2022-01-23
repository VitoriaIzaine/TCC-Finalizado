from django.urls import path
from . import views
from empresa.views import form, edit, delete, form_perfil,view_empresa

urlpatterns = [
    path('', views.principal, name='principal'),
    path('alterar_vagas/', views.alterar_vagas, name='alterar_vagas'),
    path('perfil_empresa', views.perfil_empresa, name='perfil_empresa'),
    path('cadastro_empresa/', views.cadastro_empresa, name='cadastro_empresa'),
    path('login_empresa/', views.login_empresa, name='login_empresa'),
    path('form/', form, name="form"),
    path('form_perfil/', form_perfil, name="form_perfil"),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('alterar_vagas/candidato/<int:pk>/', views.view_empresa, name='view_empresa')
]
