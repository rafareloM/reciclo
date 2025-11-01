# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View


class LoginView(View):
    """
    Login view with mocked users matching React prototype
    """
    def get(self, request):
        if request.user.is_authenticated:
            return self.redirect_by_tipo(request.user.tipo)
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Try to authenticate with email as username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.status == 'ativo':
                login(request, user)
                return self.redirect_by_tipo(user.tipo)
            else:
                messages.error(request, 'Sua conta está pendente de aprovação.')
        else:
            messages.error(request, 'Email ou senha inválidos.')

        return render(request, 'accounts/login.html')

    def redirect_by_tipo(self, tipo):
        """Redirect user based on their type"""
        if tipo == 1:
            return redirect('admin_dashboard:dashboard')
        elif tipo == 2:
            return redirect('curator:dashboard')
        elif tipo == 3:
            return redirect('producer:dashboard')
        return redirect('accounts:login')


class LogoutView(View):
    """Logout view"""
    def get(self, request):
        logout(request)
        messages.success(request, 'Você saiu com sucesso.')
        return redirect('accounts:login')
