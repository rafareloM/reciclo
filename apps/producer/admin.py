# coding: utf-8
from django.contrib import admin
from .models import Material, Coleta, Conquista, ConquistaUsuario, PontoColeta, Evento


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'produtor', 'status', 'curador', 'criado_em']
    list_filter = ['status', 'categoria', 'criado_em']
    search_fields = ['nome', 'descricao', 'produtor__username']


@admin.register(Coleta)
class ColetaAdmin(admin.ModelAdmin):
    list_display = ['material', 'produtor', 'quantidade', 'pontos', 'status', 'data_coleta']
    list_filter = ['status', 'data_coleta']
    search_fields = ['material__nome', 'produtor__username']


@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'icone', 'pontos_necessarios']
    search_fields = ['nome', 'descricao']


@admin.register(ConquistaUsuario)
class ConquistaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'conquista', 'obtido_em']
    list_filter = ['obtido_em']
    search_fields = ['usuario__username', 'conquista__nome']


@admin.register(PontoColeta)
class PontoColetaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'horario', 'ativo']
    list_filter = ['ativo']
    search_fields = ['nome', 'endereco']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'status', 'data', 'horario_inicio', 'participantes']
    list_filter = ['tipo', 'status', 'data']
    search_fields = ['titulo', 'localizacao']
