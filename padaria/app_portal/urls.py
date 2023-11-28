from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_cliente, name='login'),
    path('cadastre-se/', views.cadastre_se, name='cadastre-se'),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('login/pedidos/', views.pedidos, name='pedidos'),
    path('informacoes/', views.infomacoes, name='informacoes'),
    path('obrigado/', views.obrigado, name='obrigado'),
]
