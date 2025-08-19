# QuizApp

**QuizApp** is a Django-based web application for managing quizzes.  
It allows teachers to create quizzes, assign them to courses and batches, and allows students to take quizzes with a timer.

---

## Features
- Teacher can create quizzes for a specific course and batch.
- Quizzes can have multiple-choice questions (MCQs) with options A, B, C, D.
- Automatic timer for quizzes with auto-submit when time ends.
- Categorized quizzes: Active, Upcoming, and Previous.
- JSON-based question storage for flexibility.
- Clean, interactive, and responsive UI.

---

## Tech Stack
- **Backend:** Django 4.x  
- **Database:** PostgreSQL (JSONField for questions)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Heroku, VPS, or other hosting platforms  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/QuizApp.git
   cd QuizApp
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (e.g., `SECRET_KEY`, database credentials).

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Usage
- Access the admin panel at `/admin` to create courses, batches, teachers, and quizzes.  
- Students can access quizzes, answer questions, and submit before the timer ends.  
- Quizzes are automatically categorized as Active, Upcoming, or Previous.  

---

## Project Structure
```
QuizApp/
├─ QuizApp/         # Project settings
├─ Quiz/            # Main quiz app (models, views, templates)
├─ Teacher/         # Teacher app
├─ Batch/           # Batch app
├─ Department/      # Department app
├─ Course/          # Course app
├─ templates/       # HTML templates
├─ static/          # CSS/JS files
└─ manage.py
```

---

## Contributing
1. Fork the repository  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```
5. Open a pull request  

---

## License
MIT License © 2025 [Your Name]
