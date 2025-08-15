from django.shortcuts import render, redirect
from requests import session
from Student.views import student_panel
from Teacher.views import teacher_panel
from .forms import LoginForm
from Student.models import Student
from Teacher.models import Teacher

def user_login(request):
    
    # if user have session
    if 'user_id' in request.session:
        return redirect('quiz_list')
    
    
    form = LoginForm(request.POST or None)
    error = None

    if request.method == 'POST' and form.is_valid():
        
        
        uid = form.cleaned_data['uid']
        password = form.cleaned_data['password']
        role = form.cleaned_data['role']

        if role == 'student':
          try:
            user = Student.objects.get(uid=uid)
            if user.check_password(password):
                # Save info in session
                request.session['username']=user.name
                request.session['user_id'] = user.id
                request.session['role'] = 'student'
                
                # Pass user object to template
                return render(request, 'student_panel.html', {'user': user})
            else:
                error = "Incorrect password."
          except Student.DoesNotExist:
           error = "Student not found."

        elif role == 'teacher':
            try:
                user = Teacher.objects.get(uid=uid)
                
                
                
                if user.check_password(password):
                    request.session['username']=user.name
                    request.session['user_id'] = user.id
                    request.session['role'] = 'teacher'
                    
                    return redirect('teacher_panel')
                else:
                    error = "Incorrect password."
            except Teacher.DoesNotExist:
                error = "Teacher not found."


    return render(request, 'login.html', {'form': form, 'error': error})



def user_logout(request):
    request.session.flush()  
    return redirect('login')


def user_panel(request):
    role=request.session['role']
    
    if role=='student':
        return redirect('student_panel')
    return redirect('teacher_panel')


