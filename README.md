<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>QuizApp Documentation</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f4f6f8;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #007BFF;
        }
        pre {
            background: #e9ecef;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
        code {
            background: #f1f3f5;
            padding: 2px 6px;
            border-radius: 4px;
        }
        ul, ol {
            margin-left: 20px;
        }
        .section {
            margin-bottom: 30px;
        }
        .project-structure pre {
            background: #f8f9fa;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>QuizApp</h1>
    <p><strong>QuizApp</strong> is a Django-based web application for managing quizzes. 
    It allows teachers to create quizzes, assign them to courses and batches, and allows students to take quizzes with a timer.</p>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li>Teacher can create quizzes for a specific course and batch.</li>
            <li>Quizzes can have multiple-choice questions (MCQs) with options A, B, C, D.</li>
            <li>Automatic timer for quizzes with auto-submit when time ends.</li>
            <li>Categorized quizzes: Active, Upcoming, and Previous.</li>
            <li>JSON-based question storage for flexibility.</li>
            <li>Clean, interactive, and responsive UI.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Tech Stack</h2>
        <ul>
            <li><strong>Backend:</strong> Django 4.x</li>
            <li><strong>Database:</strong> PostgreSQL (JSONField for questions)</li>
            <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
            <li><strong>Deployment:</strong> Can be deployed on Heroku, VPS, or other hosting platforms</li>
        </ul>
    </div>

    <div class="section">
        <h2>Installation</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/yourusername/QuizApp.git
cd QuizApp</code></pre>
            </li>
            <li>Create a virtual environment and activate it:
                <pre><code>python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows</code></pre>
            </li>
            <li>Install dependencies:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Set up environment variables (e.g., SECRET_KEY, database credentials).</li>
            <li>Apply migrations:
                <pre><code>python manage.py migrate</code></pre>
            </li>
            <li>Create a superuser:
                <pre><code>python manage.py createsuperuser</code></pre>
            </li>
            <li>Run the development server:
                <pre><code>python manage.py runserver</code></pre>
            </li>
        </ol>
    </div>

    <div class="section">
        <h2>Usage</h2>
        <ul>
            <li>Access the admin panel at <code>/admin</code> to create courses, batches, teachers, and quizzes.</li>
            <li>Students can access quizzes, answer questions, and submit before the timer ends.</li>
            <li>Quizzes are automatically categorized as Active, Upcoming, or Previous.</li>
        </ul>
    </div>

    <div class="section project-structure">
        <h2>Project Structure</h2>
        <pre>
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
        </pre>
    </div>

    <div class="section">
        <h2>Contributing</h2>
        <ol>
            <li>Fork the repository</li>
            <li>Create a new branch: <code>git checkout -b feature-name</code></li>
            <li>Commit your changes: <code>git commit -m "Add new feature"</code></li>
            <li>Push to the branch: <code>git push origin feature-name</code></li>
            <li>Open a pull request</li>
        </ol>
    </div>

    <div class="section">
        <h2>License</h2>
        <p>MIT License © 2025 [Your Name]</p>
    </div>

</body>
</html>

