from django.urls import path
from . import views

urlpatterns = [
    path('teacher_panel/', views.teacher_panel, name='teacher_panel'),
    path('new_quiz/', views.create_new_quiz, name='new_quiz'),
]
