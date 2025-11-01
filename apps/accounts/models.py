# coding: utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Modelo de usuário customizado
    Corresponde a interface User em App.tsx
    """
    TIPO_CHOICES = (
        (1, 'Administrador'),
        (2, 'Curador'),
        (3, 'Produtor'),
    )

    tipo = models.IntegerField(
        choices=TIPO_CHOICES,
        default=3,
        verbose_name='Tipo de Usuário'
    )

    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('pendente', 'Pendente'),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendente',
        verbose_name='Status'
    )

    pontos = models.IntegerField(default=0, verbose_name='Pontos')

    ultima_atividade = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Atividade'
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_tipo_display()})"

    def is_admin(self):
        return self.tipo == 1

    def is_curator(self):
        return self.tipo == 2

    def is_producer(self):
        return self.tipo == 3


class Notificacao(models.Model):
    """
    Modelo de notificações para usuários
    """
    TIPO_CHOICES = (
        ('info', 'Informação'),
        ('achievement', 'Conquista'),
        ('reminder', 'Lembrete'),
    )

    usuario = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='notificacoes'
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=200)
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['-criada_em']

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"
