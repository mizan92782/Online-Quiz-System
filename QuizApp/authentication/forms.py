from django import forms

ROLE_CHOICES = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
)

class LoginForm(forms.Form):
    uid = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLE_CHOICES)
