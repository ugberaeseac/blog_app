# blog_app 

A full-featured **Blog Web Application** built with **Django**, designed for managing user-generated posts with authentication, user profiles, and categorized content. The project demonstrates scalable Django practices and clean separation of concerns across apps.

------------------------------------------------------------------------------------------------------------------------------

## Features

-   **User Authentication** -- Register, Login, Logout functionality with Django's built-in auth system.
-   **User Profiles** -- Each user can manage their own profile and view others' blogs.
-   **Blog Posts CRUD** -- Create, Read, Update, and Delete posts easily.
-   **Categories & Filtering** -- Posts organized by category, filterable by user or date.
-   **Static Files Setup** -- Proper Django static configuration using `collectstatic`.
-   **Responsive Design** -- Styled using **Bootstrap** for a clean, mobile-friendly interface.
-   **Pagination** -- Paginated post listings for better performance.
-   **Admin Dashboard** -- Manage users, posts, and categories from Django admin.

------------------------------------------------------------------------

## Tech Stack

###  Layer                      Technology
--------------------        -------------------------------------------
- **  Backend  **             Django 5.x (Python 3.10)
- **  Frontend **             HTML5, CSS3, Bootstrap, Crispy Forms
- **  Database **             SQLite3 (local), PostgreSQL (deployment via dj-database-url)
- **  Media Storage **        Cloudinary (django-cloudinary-storage)
- **  Static Handling **      WhiteNoise
- **  Environment **          Virtualenv
- **  Deployment  **          Render

------------------------------------------------------------------------

## Project Structure

    blog_app/
    │
    ├── blog/                 # Main app: posts, views, models, urls
    │   ├── templates/blog/   # HTML templates
    │   ├── static/blog/      # CSS, JS, images
    │   ├── models.py         # Post, Category models
    │   ├── views.py          # CRUD logic
    │   ├── urls.py           # URL routing
    │
    ├── users/                # Authentication and profile management
    │   ├── templates/users/
    │   ├── forms.py
    │   ├── views.py
    │   ├── urls.py
    │
    ├── blog_app/             # Project-level settings and configs
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │
    ├── staticfiles/          # Collected static files (after `collectstatic`)
    │
    ├── manage.py             # Django management script
    └── requirements.txt      # Python dependencies

------------------------------------------------------------------------

## How to Run Locally

### Clone the repository

``` bash
git clone https://github.com/ugberaeseac/blog_app.git
cd blog_app
```

### Create and activate a virtual environment

``` bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

``` bash
pip install -r requirements.txt
```

### Run database migrations

``` bash
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser (optional)

``` bash
python manage.py createsuperuser
```

### Run the development server

``` bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

------------------------------------------------------------------------

## Static Files Management

To collect static files (for deployment):

``` bash
python manage.py collectstatic --noinput
```

Ensure your static folder is properly configured in `settings.py`:

``` python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'blog' / 'static']
```

------------------------------------------------------------------------

## Future Improvements

-   Add blog post comments and reactions
-   Enable image uploads for posts
-   Add rich text editor support (like CKEditor)
-   Implement REST API using Django REST Framework (DRF)
-   Add search and recommendation features

------------------------------------------------------------------------

## Author

**Charles Ugberaese**\
Full-Stack Software Engineer \| Focused on Backend Development\
Passionate about building scalable systems that power digital trade and regional integration in Africa.

------------------------------------------------------------------------

## License

This project is licensed under the **MIT License**.
