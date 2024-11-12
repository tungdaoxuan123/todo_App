# Todo App with Django & Django REST Framework

This is a simple To-Do app built with Django and Django REST Framework.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tungdaoxuan123/todo_App
   cd TodoAPI
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

You can interact with the API at:
- POST `/api/tasks/` - Create a task
- GET `/api/tasks/` - List all tasks
- PUT/PATCH `/api/tasks/{id}/` - Update a task
- DELETE `/api/tasks/{id}/` - Delete a task
