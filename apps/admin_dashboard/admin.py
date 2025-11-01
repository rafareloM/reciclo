# coding: utf-8
from django.contrib import admin
from .models import EspacoFisico, Agendamento


@admin.register(EspacoFisico)
class EspacoFisicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'capacidade', 'disponivel', 'endereco']
    list_filter = ['tipo', 'disponivel']
    search_fields = ['nome', 'endereco', 'descricao']


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'data', 'horario_inicio', 'horario_fim', 'espaco', 'criado_por']
    list_filter = ['tipo', 'data']
    search_fields = ['titulo', 'espaco__nome']
