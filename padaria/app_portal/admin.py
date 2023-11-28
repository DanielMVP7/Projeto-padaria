from django.contrib import admin
from .models import Cliente
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 'nome_completo', 'email', 'data_nascimento', 'sexo', 'foto']