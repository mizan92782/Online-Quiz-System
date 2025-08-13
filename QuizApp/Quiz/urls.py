

from django.urls import path

from . import views  # include is needed

urlpatterns = [
    path('', views.quiz_list_view,name='quiz_list'),  # Include quiz app's URLs
    path('quiz/<int:pk>/', views.quiz,name='quizQuesition'),  # Include quiz app's URLs
]
