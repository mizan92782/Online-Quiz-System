from django.shortcuts import render
from Student.models import Student

# Create your views here.
def student_panel(request):
  
   id = request.session.get('user_id');
   student = Student.objects.get(pk=id)
   quizzes = Student.objects.filter(teacher=student)
   context={'quizzes':quizzes}

   return render(request,'student_panel.html',context)
   
  
