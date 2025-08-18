import json
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from Student.models import Student
from submission.models import Submission
from Quiz.models import Quiz
from submission.models import Submission


def quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    user_id = request.session.get('user_id')

    if not user_id:
        return HttpResponse("No user logged in. Please log in first.", status=400)

    try:
        student = Student.objects.get(pk=user_id)
    except Student.DoesNotExist:
        return HttpResponse("Student not found. Please contact admin.", status=404)

    # Check if submission already exists
    if Submission.objects.filter(quiz=quiz, student=student).exists():
        return HttpResponse("<h1>You already submitted</h1>")

    if request.method == 'POST':
        submission_json = request.POST.get("submission_json")
        print(submission_json)
        if submission_json:
            submission_data = json.loads(submission_json)
            Submission.objects.create(
                quiz=quiz,
                student=student,
                submission=submission_data,
                submitted=True
            )
            return HttpResponse("Submission saved successfully")
        else:
            return HttpResponse("No submission data received.", status=400)

    # Check quiz status
    if quiz.is_compeleted():
        status = "completed"
    elif quiz.is_active():
        status = "active"
    else:
        status = "coming"

    context = {
        'quiz': quiz,
        'status': status,
    }
    return render(request, 'quiz/quiz.html', context)
