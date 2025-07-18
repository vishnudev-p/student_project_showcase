# Student Project Showcase Portal

A simple Django web application for showcasing student projects. Admins can add, edit, and delete projects, while users can view them on a public-facing website.

## Features
- Admin panel to manage student projects
- Homepage listing all projects
- Detail page for each project
- SQLite database for easy setup
- Clean UI with Bootstrap

## Project Model Fields
- Title
- Student Name
- Department
- Short Description
- Full Description
- Optional GitHub/Demo Link

## Setup Instructions

1. **Clone the repository** (if using version control):
   ```bash
   git clone <repo-url>
   cd student_project_showcase
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install Django:**
   ```bash
   pip install django
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for the admin panel:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the site:**
   - Homepage: [http://localhost:8000/](http://localhost:8000/)
   - Admin panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Usage
- Add, edit, or delete projects via the admin panel.
- Users can browse all projects and view details on the homepage.

## Notes
- No authentication is required for viewing projects.
- For any issues, refer to the Django documentation: https://docs.djangoproject.com/ 


