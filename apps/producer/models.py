# coding: utf-8
from django.db import models
from apps.accounts.models import CustomUser


class Material(models.Model):
    """
    Modelo de material publicado
    Corresponde a interface PublishedItem em components/producer/PublishSection.tsx
    """
    CATEGORIA_CHOICES = (
        ('plastico', 'Pl�stico'),
        ('vidro', 'Vidro'),
        ('papel', 'Papel'),
        ('metal', 'Metal'),
        ('eletronicos', 'Eletr�nicos'),
        ('organico', 'Org�nico'),
    )

    STATUS_CHOICES = (
        ('pending', 'Aguardando Curadoria'),
        ('approved', 'Aprovado'),
        ('rejected', 'Reprovado'),
    )

    nome = models.CharField(max_length=200, verbose_name='Nome')
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        verbose_name='Categoria'
    )
    descricao = models.TextField(verbose_name='Descri��o')
    localizacao = models.CharField(max_length=300, verbose_name='Localiza��o')

    produtor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='materiais_publicados',
        limit_choices_to={'tipo': 3}
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Status'
    )

    feedback_curador = models.TextField(
        blank=True,
        null=True,
        verbose_name='Feedback do Curador'
    )

    curador = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='materiais_revisados',
        limit_choices_to={'tipo': 2}
    )

    imagem = models.ImageField(
        upload_to='materiais/%Y/%m',
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.nome} - {self.produtor.get_full_name()}"


class Coleta(models.Model):
    """
    Modelo de coleta realizada
    Corresponde a MOCK_HISTORY em components/producer/HistorySection.tsx
    """
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='coletas'
    )

    produtor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='coletas_realizadas'
    )

    quantidade = models.CharField(max_length=50, verbose_name='Quantidade')
    pontos = models.IntegerField(verbose_name='Pontos Ganhos')

    STATUS_CHOICES = (
        ('agendado', 'Agendado'),
        ('coletado', 'Coletado'),
        ('cancelado', 'Cancelado'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='agendado'
    )

    feedback = models.TextField(
        blank=True,
        null=True,
        verbose_name='Feedback'
    )

    data_coleta = models.DateField(verbose_name='Data da Coleta')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Coleta'
        verbose_name_plural = 'Coletas'
        ordering = ['-data_coleta']

    def __str__(self):
        return f"Coleta {self.material.nome} - {self.data_coleta}"


class Conquista(models.Model):
    """
    Modelo de conquistas/achievements
    Corresponde a ACHIEVEMENTS em components/producer/HistorySection.tsx
    """
    nome = models.CharField(max_length=100, verbose_name='Nome')
    icone = models.CharField(max_length=10, verbose_name='�cone (emoji)')
    descricao = models.TextField(verbose_name='Descri��o')
    pontos_necessarios = models.IntegerField(verbose_name='Pontos Necess�rios')

    class Meta:
        verbose_name = 'Conquista'
        verbose_name_plural = 'Conquistas'

    def __str__(self):
        return self.nome


class ConquistaUsuario(models.Model):
    """
    Rela��o entre usu�rio e conquistas obtidas
    """
    usuario = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='conquistas'
    )
    conquista = models.ForeignKey(
        Conquista,
        on_delete=models.CASCADE
    )
    obtido_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Conquista do Usu�rio'
        verbose_name_plural = 'Conquistas dos Usu�rios'
        unique_together = ('usuario', 'conquista')

    def __str__(self):
        return f"{self.usuario.username} - {self.conquista.nome}"


class PontoColeta(models.Model):
    """
    Modelo de pontos de coleta
    Corresponde a COLLECTION_POINTS em components/producer/PublishSection.tsx
    """
    nome = models.CharField(max_length=200, verbose_name='Nome')
    endereco = models.CharField(max_length=300, verbose_name='Endere�o')
    horario = models.CharField(max_length=100, verbose_name='Hor�rio')
    distancia = models.CharField(max_length=50, verbose_name='Dist�ncia', blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ponto de Coleta'
        verbose_name_plural = 'Pontos de Coleta'

    def __str__(self):
        return self.nome


class Evento(models.Model):
    """
    Modelo de eventos ao vivo
    Corresponde a EVENTS_TODAY em components/producer/MapSection.tsx
    """
    titulo = models.CharField(max_length=200, verbose_name='Título')
    localizacao = models.CharField(max_length=300, verbose_name='Localização')
    horario_inicio = models.TimeField(verbose_name='Horário de Início')
    horario_fim = models.TimeField(verbose_name='Horário de Fim')
    data = models.DateField(verbose_name='Data')

    TIPO_CHOICES = (
        ('coleta', 'Coleta'),
        ('evento', 'Evento'),
        ('workshop', 'Workshop'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    STATUS_CHOICES = (
        ('programado', 'Programado'),
        ('em_andamento', 'Em Andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='programado'
    )

    participantes = models.IntegerField(default=0, verbose_name='Participantes')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data', 'horario_inicio']

    def __str__(self):
        return f"{self.titulo} - {self.data}"
