# jmatsika.com — Personal Website & Portfolio

A fully featured Django-based personal website and portfolio with a working contact form, production-ready static file handling, and secure deployment. This project showcases real-world Django deployment practices including Nginx configuration, Gunicorn setup, and email integration.

## Features

### Core Website Features

- **Responsive Design** (Portfolio and landing pages optimized for all devices)
- **Contact Form** (Sends messages directly to email via Gmail SMTP)
- **Django-Powered Backend** (Clean, maintainable architecture)
- **Secure Configuration** (Environment variables for sensitive data)

### Database & Configuration

- **PostgreSQL** as the production database
- **SQLite** for local development
- **Separate Settings** (Development and production configurations)
- **python-decouple** for environment variable management

### Static Files & Assets

- **Django collectstatic** for production asset management
- **Nginx** configured to serve static files directly
- **Optimized Loading** (Cacheable assets for better performance)

### Deployment & DevOps

- **Linux (Ubuntu)** server setup
- **Gunicorn** as the WSGI application server
- **Nginx Reverse Proxy** configuration
- **Gmail SMTP** integration for email delivery
- **Secure Environment Variables** configuration

## Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL (Production), SQLite (Development)
- **Templating:** Django Templates
- **Server:** Linux (Ubuntu)
- **WSGI Server:** Gunicorn
- **Web Server & Proxy:** Nginx
- **Email:** Gmail SMTP
- **Tools:** VS Code, Postman, Git & GitHub

## Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/pasej5/jmatsika-website.git
cd jmatsika-website
```

### 2. Create a Virtual Environment & Install Dependencies

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```sh
python manage.py migrate
```

### 5. Collect Static Files

```sh
python manage.py collectstatic
```

### 6. Run the Application

```sh
python manage.py runserver
```

## Deployment Guide

### 1. Set Up Production Environment

- Set up an Ubuntu server
- Install Python, PostgreSQL, and necessary dependencies
- Clone the repository and install requirements

### 2. Configure Gunicorn

```sh
gunicorn jmatsika_website.wsgi:application --bind 0.0.0.0:8000
```

### 3. Configure Nginx

- Set up Nginx as a reverse proxy
- Configure Nginx to serve static files from `/staticfiles/`
- Set up SSL for HTTPS (recommended)


## What I Learned

- Real-world Django deployment workflow
- Debugging production static file issues
- Managing permissions and ownership on Linux servers
- Nginx configuration for Django applications
- Separating development and production settings properly
- Handling email services securely
- Why things work locally but fail in production 😄

## Live Website

🔗 **https://www.jmatsika.com**

## Author

**Jealous Matsikachando**  
Full Stack Software Engineer

- Website: https://www.jmatsika.com
- GitHub: https://github.com/pasej5

## Contributing

Feel free to fork this repository, open issues, and submit pull requests!

## License
