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
├── react-prototype/               # UI/UX reference (Figma design)
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
- **Database**: SQLite (development) / PostgreSQL (recommended for production)
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

## 🎨 UI/UX Reference

The `react-prototype/` directory contains a Figma-generated React prototype used as a design reference. The Django implementation matches this design using:

- **Tailwind CSS** for styling
- **Alpine.js** for interactivity
- **Green sustainability theme** (#16a34a)
- **Responsive design** principles

To view the React prototype:
```bash
cd react-prototype
npm install
npm run dev
# Open http://localhost:3000
```

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

Run tests for all apps:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test apps.producer
```

## 🚀 Production Deployment

For production deployment:

1. **Update settings.py**: Set DEBUG=False, configure ALLOWED_HOSTS, use environment variables
2. **Use PostgreSQL** instead of SQLite
3. **Collect static files**: `python manage.py collectstatic`
4. **Use a production server** (Gunicorn, uWSGI)

## 📚 Additional Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Tailwind CSS**: https://tailwindcss.com/
- **Alpine.js**: https://alpinejs.dev/
- **Project Instructions**: See `CLAUDE.md` for detailed development guidelines

## 👥 Authors

Built with Django and designed for sustainability.

---

**Re-Ciclo** - Making recycling accessible and rewarding 🌍♻️
