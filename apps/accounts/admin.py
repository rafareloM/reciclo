# coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Notificacao


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'tipo', 'status', 'pontos']
    list_filter = ['tipo', 'status', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('tipo', 'status', 'pontos', 'ultima_atividade')}),
    )


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'tipo', 'lida', 'criada_em']
    list_filter = ['tipo', 'lida', 'criada_em']
    search_fields = ['titulo', 'mensagem', 'usuario__username']
