from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from Department.models import Department  # Assuming you have a Department model

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    uid = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128, default="teacher123")

    status = models.CharField(max_length=30)  # e.g., Lecturer, Assistant Professor
    join_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.uid})"
    
    def check_password(self,rawpassword):
        return self.password==rawpassword;
    
    
    def save(self, *args, **kwargs):
        # Format fields before saving
        if self.name:
            self.name = self.name.title()
        if self.status:
            self.status = self.status.title()
        # Example uid: DEPCode + "T" + 3-digit ID
        dep_code = self.department.title;
        next_id = (Teacher.objects.count() + 1)
        self.uid = f"{dep_code} {next_id}"
    

        super().save(*args, **kwargs)
