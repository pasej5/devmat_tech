# Copilot Instructions for AI Coding Agents

## Project Overview
This is a Django-based web application. The main components are:
- `jmatsika_website/`: Django project settings and configuration.
- `landing_page/`: Django app for the landing page, including models, views, URLs, static assets, and templates.

## Architecture & Data Flow
- The app follows standard Django MVC (Model-View-Template) architecture.
- Static files (CSS, JS, images, fonts) are organized under `landing_page/static/`.
- HTML templates are in `landing_page/templates/landing_page/`.
- Database is SQLite (`db.sqlite3`).

## Developer Workflows
- **Run server:** `python manage.py runserver`
- **Migrations:**
  - Make migrations: `python manage.py makemigrations`
  - Apply migrations: `python manage.py migrate`
- **Run tests:** `python manage.py test`
- **Admin:** Register models in `landing_page/admin.py` for Django admin access.

## Project-Specific Patterns
- Static assets are manually managed; reference them in templates using Django's `{% static %}` tag.
- Templates are organized by page type (e.g., `index.html`, `about.html`).
- App-specific URLs are defined in `landing_page/urls.py` and included in the project's `jmatsika_website/urls.py`.
- Models are defined in `landing_page/models.py` and use Django ORM.

## Integration Points
- No external APIs or services detected; all logic is local to Django.
- All cross-component communication is via Django's standard mechanisms (views, models, templates).

## Conventions
- Use Django's built-in management commands for all workflows.
- Organize static files by type (css, js, images, fonts, sass).
- Place new templates in `landing_page/templates/landing_page/`.
- Register new models in `landing_page/admin.py` for admin access.

## Key Files & Directories
- `manage.py`: Entry point for Django commands.
- `jmatsika_website/settings.py`: Project settings.
- `landing_page/models.py`: Data models.
- `landing_page/views.py`: Page logic.
- `landing_page/static/`: Static assets.
- `landing_page/templates/landing_page/`: HTML templates.

## Example: Adding a New Page
1. Create a template in `landing_page/templates/landing_page/`.
2. Add a view in `landing_page/views.py`.
3. Map the view in `landing_page/urls.py`.
4. Reference static assets using `{% static '...' %}`.

---
For questions or missing conventions, ask for clarification or review related Django documentation.
