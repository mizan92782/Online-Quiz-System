from time import timezone
from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from django.shortcuts import render
from .models import Quiz

def quiz_list_view(request):
    quizzes = Quiz.objects.all()

    active_quizzes = [quiz for quiz in quizzes if quiz.is_active()]
    upcoming_quizzes = [quiz for quiz in quizzes if quiz.is_comming()]
    previous_quizzes = [quiz for quiz in quizzes if quiz.is_compeleted()]

    return render(request, 'quiz/quiz_list.html', {
        'active_quizzes': active_quizzes,
        'upcoming_quizzes': upcoming_quizzes,
        'previous_quizzes': previous_quizzes,
    })
    


from django.shortcuts import get_object_or_404

def quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    
    # Check if quiz is active
    now = timezone.now()
    if quiz.is_compeleted():
        status = "completed"
    elif quiz.is_active():
        status = "active"
    else:
        status = "coming"
    
    context = {
        'quiz': quiz,
        'status': status,
        'now': now
    }
    return render(request, 'quiz/quiz.html',context)
