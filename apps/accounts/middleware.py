# coding: utf-8
from django.shortcuts import redirect
from django.urls import reverse


class RoleBasedAccessMiddleware:
    """
    Middleware to enforce role-based access control
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access to login, logout, static files, and admin
        if request.path.startswith('/login') or \
           request.path.startswith('/logout') or \
           request.path.startswith('/static') or \
           request.path.startswith('/media') or \
           request.path.startswith('/admin'):
            return self.get_response(request)

        # Check authentication
        if request.user.is_authenticated:
            # Check user status
            if request.user.status != 'ativo':
                # Only allow logout for non-active users
                if not request.path.startswith('/logout'):
                    return redirect('accounts:login')

        response = self.get_response(request)
        return response
