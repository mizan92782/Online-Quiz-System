from django.urls import path
from . import views

urlpatterns = [
    path('student_panel/', views.student_panel, name='student_panel'),
]
