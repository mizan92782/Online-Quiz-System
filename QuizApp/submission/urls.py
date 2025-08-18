from . import views
from django.urls import path

urlpatterns=[
  path('quiz/<int:pk>/', views.quiz,name='quizQuesition'), 
]