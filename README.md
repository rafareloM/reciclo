# Re-Ciclo 🌱

**Re-Ciclo** is a Django-based sustainability and recycling platform with role-based dashboards for managing recyclable materials, collection points, and events.

![Django](https://img.shields.io/badge/Django-5.2-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38bdf8?logo=tailwindcss)
![Alpine.js](https://img.shields.io/badge/Alpine.js-3.x-8bc0d0?logo=alpine.js)

## 🎯 Features

### Role-Based Dashboards

**Producer Dashboard (Produtor)** - 3 Tabs:
- **History**: View collection history, earned points, and unlocked achievements
- **Publish**: Submit recyclable materials for approval and view collection points
- **Map/Events**: See live events, notifications, and interactive map

**Curator Dashboard (Curador)**:
- Review and approve/reject materials submitted by producers
- Provide feedback on submissions
- Track review history and statistics

**Admin Dashboard (Administrador)** - 3 Tabs:
- **Physical Spaces**: Manage collection locations and event venues (CRUD)
- **Calendar**: Schedule events and view upcoming activities
- **User Management**: Approve/reject user registrations and manage permissions

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd reciclo
   ```

2. **Install dependencies**
   ```bash
   pip install django pillow
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create demo users**
   ```bash
   python manage.py create_demo_users
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**

   Open your browser and navigate to: **http://127.0.0.1:8000**

### 🔑 Demo Credentials

| Role | Email | Password |
|------|-------|----------|
| **Producer** | produtor@reciclo.com | senha123 |
| **Curator** | curador@reciclo.com | senha123 |
| **Admin** | admin@reciclo.com | senha123 |

## 📁 Project Structure

```
reciclo/
├── apps/                          # Django applications
│   ├── accounts/                  # Authentication & user management
│   ├── producer/                  # Producer functionality
│   ├── curator/                   # Curator functionality
│   └── admin_dashboard/           # Admin functionality
├── templates/                     # HTML templates
├── static/                        # Static files (CSS, JS, images)
├── media/                         # User-uploaded files
├── reciclo/                       # Django project configuration
└── manage.py                      # Django management script
```

## 🗄️ Database Models

### User Models (accounts)
- **CustomUser**: Extended user model with `tipo` (role), `status`, and `pontos` (points)
- **Notificacao**: User notifications system

### Producer Models (producer)
- **Material**: Recyclable materials submitted by producers
- **Coleta**: Collection history with points tracking
- **Conquista**: Achievement definitions (badges)
- **ConquistaUsuario**: User achievements (many-to-many)
- **PontoColeta**: Collection points/locations
- **Evento**: Live events for the map view

### Admin Models (admin_dashboard)
- **EspacoFisico**: Physical spaces for collections/events
- **Agendamento**: Event scheduling and calendar

## 🎨 Technology Stack

- **Backend**: Django 5.2 (Python)
- **Frontend**: HTML templates with Tailwind CSS
- **Interactivity**: Alpine.js for dynamic components
- **Database**: SQLite - Will use mySQL afterwards.
- **Authentication**: Django built-in auth with custom user model

## 🔧 Development Commands

```bash
# Create a new Django app
python manage.py startapp app_name

# Make database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (for Django admin)
python manage.py createsuperuser

# Create demo users
python manage.py create_demo_users

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Access Django admin panel
# Navigate to http://127.0.0.1:8000/admin/
```

## 🎯 User Workflows

### Producer Workflow
1. Register and wait for admin approval
2. Login and access Producer Dashboard
3. Submit recyclable materials for curator review
4. Track collection history and earn points
5. Unlock achievements based on points
6. View collection points and live events

### Curator Workflow
1. Login with curator credentials
2. Review pending materials
3. Approve materials or reject with feedback
4. Track review history and statistics

### Admin Workflow
1. Login with admin credentials
2. Approve/reject new user registrations
3. Manage physical spaces (add/edit/delete)
4. Schedule events on the calendar
5. Monitor system activity

## 🔐 Authentication & Permissions

The application uses role-based access control with three user types:

- **Type 1 (Administrador)**: Full system access
- **Type 2 (Curador)**: Material review and approval
- **Type 3 (Produtor)**: Submit materials and track collections

Access is enforced through:
- Custom decorators: `@admin_required`, `@curator_required`, `@producer_required`
- Middleware: `RoleBasedAccessMiddleware`
- User status check: Only `ativo` (active) users can login

## 🎨 Design System

The application uses a consistent design system with:

- **Tailwind CSS** for styling
- **Alpine.js** for interactivity
- **Green sustainability theme** (#16a34a)
- **Responsive design** principles

## 📝 Configuration

### Environment Settings

Key settings in `reciclo/settings.py`:

```python
# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Language and timezone
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Static and media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
```

## 🧪 Testing

### Running Tests

Run all tests across the entire project:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test apps.producer
python manage.py test apps.curator
python manage.py test apps.accounts
```

Run a specific test class:
```bash
python manage.py test apps.producer.tests.MaterialTests
```

Run tests with verbose output:
```bash
python manage.py test --verbosity=2
```

### Writing Tests

Tests are organized in each app's `tests.py` file. Example test structure:

```python
from django.test import TestCase, Client
from apps.accounts.models import CustomUser
from apps.producer.models import Material

class MaterialTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = CustomUser.objects.create_user(
            username='testproducer@test.com',
            email='testproducer@test.com',
            password='testpass123',
            tipo=3,
            status='ativo'
        )
        self.client = Client()

    def test_create_material(self):
        # Test material creation
        self.client.login(username='testproducer@test.com', password='testpass123')
        response = self.client.post('/produtor/publicar/', {
            'nome': 'Test Material',
            'categoria': 'plastico',
            'descricao': 'Test description'
        })
        self.assertEqual(Material.objects.count(), 1)
```

### Test Coverage

To check test coverage, install coverage:
```bash
pip install coverage
```

Run tests with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
coverage html  # Generates HTML report in htmlcov/
```

## 📚 Additional Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Tailwind CSS**: https://tailwindcss.com/
- **Alpine.js**: https://alpinejs.dev/
- **Django Testing**: https://docs.djangoproject.com/en/5.2/topics/testing/

## 👥 Authors
Rafael M. [@rafareloM](github.com/rafareloM)

Built with Django and designed for sustainability.

---

**Re-Ciclo** - Making recycling accessible and rewarding 🌍♻️
