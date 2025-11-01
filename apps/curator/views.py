# coding: utf-8
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from apps.accounts.decorators import curator_required


@method_decorator(curator_required, name='dispatch')
class CuratorDashboardView(View):
    """Curator dashboard with mocked data from React prototype"""
    def get(self, request):
        return render(request, 'curator/dashboard.html')
