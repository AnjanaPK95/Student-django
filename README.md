# Django Student Database API

This project implements a Django API for managing student records using Django REST Framework.

## Installation

### Prerequisites

Make sure you have Python and Django installed on your system.

### Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/AnjanaPK95/Student-django.git
cd Student-django
```

### Install Dependencies
Install required Python packages using pip and requirements.txt:

```bash
pip install -r requirements.txt
```

This will install Django and other necessary packages specified in requirements.txt.

### Database Setup
Configure your database settings in settings.py. By default, this project uses SQLite.
```bash
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Run migrations to create database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```
### Running the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at http://localhost:8000/api/students/






