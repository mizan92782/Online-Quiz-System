from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'batch',
            'department',
            'course',
            'quiz_no',
            'quiz_marks',
            'question',
            'start',
            'end',
        ]
        
        
        exclude = ['teacher','quiz_marks']
        
        
        widgets = {
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'question': forms.HiddenInput(),  # hide from user
             # hide from user
        }
