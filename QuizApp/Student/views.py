from django.shortcuts import render
from Student.models import Student
from Student.models import Student
from submission.models import Submission

# Create your views here.
def student_panel(request):
  
   id = request.session.get('user_id');
   student = Student.objects.get(pk=id)
   result_published = Submission.objects.filter(
    student=student,
    quiz__published=True   
    )   
   
   result_not_published = Submission.objects.filter(
      student=student,
    quiz__published=False 
      )
   
   
   context={
      'published_result':result_published,
      'not_published_result':result_not_published
   }

   return render(request,'student_panel.html',context)
   
  
