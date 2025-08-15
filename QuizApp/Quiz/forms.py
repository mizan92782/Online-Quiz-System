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
        
        
        exclude = ['teacher']
        
        
        widgets = {
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'question': forms.HiddenInput(),  # hide from user
            'quiz_marks': forms.HiddenInput(),  # hide from user
        }
