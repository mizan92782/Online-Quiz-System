from django.shortcuts import render,redirect
from   Quiz.models  import Quiz
from Teacher.models import Teacher
from Quiz.forms import QuizForm



# Create your views here.

def teacher_panel(request):
  
   id = request.session.get('user_id');
   teacher = Teacher.objects.get(pk=id)
   quizzes = Quiz.objects.filter(teacher=teacher)
   context={'quizzes':quizzes}

   return render(request,'teacher_panel.html',context)
   
  




def create_new_quiz(request):
     
    print("get new quiz")
    if request.method == "POST":
        print("post new Quiz")
        user_id = request.session['user_id']
        teacher = Teacher.objects.get(pk=user_id)

        form = QuizForm(request.POST)
        if form.is_valid():
            print("save new quiz")
            quiz = form.save(commit=False)
            quiz.teacher = teacher

            # Assign questions JSON from hidden field
            quiz.question = form.cleaned_data['question']  # JSON string from JS
            print("save quiz in quiz model")
            quiz.save()
            return redirect('quiz_list')  # Redirect after saving
        else:
           print(form.errors) 
    else:
        form = QuizForm()

    return render(request, 'quiz_form.html', {'form': form})
