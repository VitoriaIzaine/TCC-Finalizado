"""job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path, include
from django.contrib import admin
from home import views
from empresa.views import create, edit, update, form, delete, form_perfil, create_empresa,view_candidato
from jovem.views import candidato, create_candidatar
from jovem.views import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('lei/', views.lei, name='lei'),
                  path('parceiros/', views.parceiros, name='parceiros'),
                  path('sobre/', views.sobre, name='sobre'),
                  path('dicas/', views.dicas, name='dicas'),
                  path('gerador/', views.gerador, name='gerador'),
                  path('op/', views.op, name='op'),
                  path('op_login/', views.op_login, name='op_login'),
                  path('admin/', admin.site.urls),
                  path('jovem/', include('jovem.urls')),
                  path('empresa/', include('empresa.urls')),
                  path('create/', create, name="create"),
                  path('create_empresa/', create_empresa, name="create_empresa"),
                  path('create_candidatar/', create_candidatar, name="create_candidatar"),
                  path('empresa/alterar_vagas/edit/<int:pk>/', edit, name='edit'),
                  path('update/<int:pk>/', update, name='update'),
                  path('view/<int:pk>/', view, name='view'),
                  path('view_candidato/<int:pk>/', view_candidato, name="view_candidato"),
                  path('form/', form, name="form"),
                  path('delete/<int:pk>/', delete, name='delete'),
                  path('alterar_vagas/form_perfil/', form_perfil, name="form_perfil"),
                  path('candidato<int:pk>/', candidato, name='candidato'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
