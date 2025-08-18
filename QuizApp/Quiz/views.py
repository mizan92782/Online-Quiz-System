
# Create your views here.

from itertools import batched
import django.db
from django.shortcuts import render

from Teacher.models import Teacher
from Student.models import Student
from Teacher.models import Teacher
from .models import Quiz

def quiz_list_view(request):
    quizzes = None
    
    if request.session['role']=='student':
        student_id= request.session.get('user_id')
        student= Student.objects.get(pk=student_id)
        quizzes= Quiz.objects.filter(
            batch=student.batch,
            department=student.department
            )
        
    else:
        teacher_id= request.session.get('user_id')
        teacher= Teacher.objects.get(pk=teacher_id)
        quizzes= Quiz.objects.filter(teacher=teacher)

    active_quizzes = [quiz for quiz in quizzes if quiz.is_active()]
    upcoming_quizzes = [quiz for quiz in quizzes if quiz.is_comming()]
    previous_quizzes = [quiz for quiz in quizzes if quiz.is_compeleted()]

    return render(request, 'quiz/quiz_list.html', {
        'active_quizzes': active_quizzes,
        'upcoming_quizzes': upcoming_quizzes,
        'previous_quizzes': previous_quizzes,
    })
    


