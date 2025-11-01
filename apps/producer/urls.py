# coding: utf-8
from django.urls import path
from .views import ProducerDashboardView

app_name = 'producer'

urlpatterns = [
    path('', ProducerDashboardView.as_view(), name='dashboard'),
]
