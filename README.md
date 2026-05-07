# Todo_Django_App
A Django-based Todo application with user authentication where each user can manage their own tasks with features like create, update, delete, and mark tasks as completed with timestamps.

A simple yet powerful Todo application built using Django that allows users to manage their daily tasks efficiently.

-----------------------------

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 👤 User-specific private task lists
- 📝 Create new tasks
- ✏️ Update existing tasks
- ❌ Delete tasks
- ✅ Mark tasks as completed
- 🕒 Task creation & completion timestamps
- 🔒 Password validation during registration
- 🎨 Responsive UI using Bootstrap


-----------------------------

## 🛠️ Tech Stack

- Python
- Django
- SQLite (default database)
- Bootstrap (for styling)

-----------------------------

## 📂 Project Structure

Todo_Django_App/
│
├── todo_project/
│   ├── manage.py
│   ├── todo/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── templates/
│   │
│   └── todo_project/
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
│
└── README.md

-----------------------------

## ⚙️ Installation & Setup

1. Clone the repository:
'bash'
git clone https://github.com/your-username/Todo_Django_App.git
cd Todo_Django_App

2. Create virtual environment:
'bash'
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies:
'bash'
pip install django

4. Apply migrations:
'bash'
python manage.py makemigrations
python manage.py migrate

5. Run server:
'bash'
python manage.py runserver

6. Open in browser:
http://127.0.0.1:8000/

----------------------------

📸 Features Overview

a. Add tasks with timestamps
b. Mark tasks as completed
c. View completed and pending tasks
d. Secure user-specific task management

-----------------------------

🎯 Future Improvements

🔥 AJAX-based task updates (no page reload)
📱 REST API with Django REST Framework
🔐 JWT Authentication

-----------------------------
URL

Link to LIVE app : https://srinjay.pythonanywhere.com/login/?next=/
Paste The Above Link to Your Browser And Check My Todo_Application

-----------------------------

👨‍💻 Author

Srinjay Kumar
Django Developer | Aspiring Backend & AI/ML Engineer
