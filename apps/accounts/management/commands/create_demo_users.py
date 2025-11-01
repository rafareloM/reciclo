# coding: utf-8
from django.core.management.base import BaseCommand
from apps.accounts.models import CustomUser


class Command(BaseCommand):
    help = 'Create demo users for testing'

    def handle(self, *args, **kwargs):
        # Create producer user
        if not CustomUser.objects.filter(username='produtor@reciclo.com').exists():
            user = CustomUser.objects.create_user(
                username='produtor@reciclo.com',
                email='produtor@reciclo.com',
                password='senha123',
                first_name='João',
                last_name='Produtor',
                tipo=3,
                status='ativo'
            )
            self.stdout.write(self.style.SUCCESS('Producer user created: produtor@reciclo.com'))

        # Create curator user
        if not CustomUser.objects.filter(username='curador@reciclo.com').exists():
            user = CustomUser.objects.create_user(
                username='curador@reciclo.com',
                email='curador@reciclo.com',
                password='senha123',
                first_name='Maria',
                last_name='Curadora',
                tipo=2,
                status='ativo'
            )
            self.stdout.write(self.style.SUCCESS('Curator user created: curador@reciclo.com'))

        # Create admin user
        if not CustomUser.objects.filter(username='admin@reciclo.com').exists():
            user = CustomUser.objects.create_user(
                username='admin@reciclo.com',
                email='admin@reciclo.com',
                password='senha123',
                first_name='Admin',
                last_name='Sistema',
                tipo=1,
                status='ativo',
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(self.style.SUCCESS('Admin user created: admin@reciclo.com'))

        self.stdout.write(self.style.SUCCESS('All demo users created successfully!'))
