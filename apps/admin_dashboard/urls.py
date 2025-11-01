# coding: utf-8
from django.urls import path
from .views import AdminDashboardView

app_name = 'admin_dashboard'

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='dashboard'),
]
