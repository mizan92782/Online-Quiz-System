# QuizApp

**Online Quiz System** is a Django-based web application for managing quizzes of a institute.  
It allows teachers to create quizzes, assign them to courses and batches, and allows students to take quizzes with a timer.

---

## Features
-Teacher can create quizzes with time categorized as Active, Upcoming, and Previous.
-Teacher can create quizzes for a specific course and batch.
-Quizzes can have multiple-choice questions (MCQs) with options A, B, C, D and different marks.
-JSON-based question storage for flexibility in the number of questions and marks.
-On the home page, a teacher only sees quizzes created by him (Active, Upcoming, Previous).
-In the teacher dashboard, the teacher can view quizzes that are time-up and control whether results are published or not.
-Students can see quizzes assigned to them (based on batch and department).
-Automatic timer for quizzes with auto-submit when time ends.
-In the student dashboard, students can see quizzes they have attempted as well as the quizzes where the teacher has published or not published the results.
-Clean, interactive, and responsive UI.
---

## Tech Stack
- **Backend:** Django   
- **Database:** PostgreSQL (JSONField for questions)  
- **Frontend:** HTML, CSS, JavaScript  


---

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:mizan92782/Online-Quiz-System.git
   cd Online-Quiz-System
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
├─ submisson        # Quiz submissions app
├─ Student          # Student app
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
MIT License © 2025 [Mizanur Rahman]
