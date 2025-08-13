from django.db import models
from django.utils import timezone
from Teacher.models import Teacher
from Batch.models import Batch
from Department.models import Department
from Course.models import Course

class Quiz(models.Model):
    title=models.CharField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    
    quiz_no =models.IntegerField(default=1)
    quiz_marks = models.IntegerField(default=10)
    question = models.JSONField()  # Requires Django 3.1+ and PostgreSQL

    start = models.DateTimeField()
    end = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    

    def is_active(self):
        now = timezone.now()
        return self.start <= now <= self.end
    
    def is_comming(self):
        now = timezone.now()
        return self.start > now 
    
    def is_compeleted(self):
        now = timezone.now()
        return self.end < now 



    def __str__(self):
        return f"Quiz for {self.course.courseCode} - {self.batch.batch} - {self.teacher.name}"
    def save(self,*args, **kwargs):
        self.title= f'{self.course.courseCode}-{self.course.courseName} : {self.batch} - Quiz no : {self.quiz_no}'
        
        return super().save()