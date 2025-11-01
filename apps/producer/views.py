# coding: utf-8
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from apps.accounts.decorators import producer_required


@method_decorator(producer_required, name='dispatch')
class ProducerDashboardView(View):
    """Producer dashboard with mocked data from React prototype"""
    def get(self, request):
        return render(request, 'producer/dashboard.html')
