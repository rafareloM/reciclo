# coding: utf-8
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from apps.accounts.decorators import admin_required


@method_decorator(admin_required, name='dispatch')
class AdminDashboardView(View):
    """Admin dashboard with mocked data from React prototype"""
    def get(self, request):
        return render(request, 'admin/dashboard.html')
