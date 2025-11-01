# coding: utf-8
from django.db import models
from apps.accounts.models import CustomUser


class EspacoFisico(models.Model):
    """
    Modelo de espa�os f�sicos
    Corresponde a interface Space em components/admin/SpacesManagement.tsx
    """
    TIPO_CHOICES = (
        ('coleta', 'Coleta'),
        ('curso', 'Curso'),
        ('evento', 'Evento'),
    )

    nome = models.CharField(max_length=200, verbose_name='Nome')
    endereco = models.CharField(max_length=300, verbose_name='Endere�o')
    capacidade = models.IntegerField(verbose_name='Capacidade (pessoas)')
    horario = models.CharField(max_length=100, verbose_name='Hor�rio de Funcionamento')
    descricao = models.TextField(verbose_name='Descri��o')
    disponivel = models.BooleanField(default=True, verbose_name='Dispon�vel')
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        verbose_name='Tipo'
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Espa�o F�sico'
        verbose_name_plural = 'Espa�os F�sicos'

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    """
    Modelo de agendamentos/eventos
    Corresponde a interface Event em components/admin/CalendarView.tsx
    """
    titulo = models.CharField(max_length=200, verbose_name='T�tulo')
    espaco = models.ForeignKey(
        EspacoFisico,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    data = models.DateField(verbose_name='Data')
    horario_inicio = models.TimeField(verbose_name='Hor�rio de In�cio')
    horario_fim = models.TimeField(verbose_name='Hor�rio de Fim')
    tipo = models.CharField(
        max_length=10,
        choices=EspacoFisico.TIPO_CHOICES,
        verbose_name='Tipo'
    )

    criado_por = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='agendamentos_criados'
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['data', 'horario_inicio']

    def __str__(self):
        return f"{self.titulo} - {self.data}"
