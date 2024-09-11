# My Django Portfolio Website

This is a Django-based portfolio website that includes a blog, projects section, and contact page.

## Features

- Blog with rich text editing using CKEditor
- Projects showcase
- Contact page
- Responsive design

## Technologies Used

- Django 4.2.9
- django-ckeditor 6.7.0
- django-solo 2.2.0
- Pillow 10.2.0

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/admin/` to access the admin panel and start adding content.

## Project Structure

- `mysite/`: Main project directory
- `portfolio/`: Main app directory
- `static/`: Static files (CSS, JavaScript, images)
- `media/`: User-uploaded files
- `templates/`: HTML templates

## Configuration

The main configuration file is `mysite/settings.py`.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing

The code in this project is licensed under MIT license.
