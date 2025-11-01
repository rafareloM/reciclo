# coding: utf-8
from django.urls import path
from .views import CuratorDashboardView

app_name = 'curator'

urlpatterns = [
    path('', CuratorDashboardView.as_view(), name='dashboard'),
]
