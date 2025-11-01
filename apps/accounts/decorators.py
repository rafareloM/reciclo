# coding: utf-8
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def user_type_required(allowed_types):
    """
    Decorator to restrict access based on user type
    allowed_types: list of integers [1, 2, 3]
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login')

            if request.user.tipo not in allowed_types:
                messages.error(request, 'Você não tem permissão para acessar esta página.')
                return redirect('accounts:login')

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def admin_required(view_func):
    """Decorator for admin-only views (tipo=1)"""
    return user_type_required([1])(view_func)


def curator_required(view_func):
    """Decorator for curator-only views (tipo=2)"""
    return user_type_required([2])(view_func)


def producer_required(view_func):
    """Decorator for producer-only views (tipo=3)"""
    return user_type_required([3])(view_func)
