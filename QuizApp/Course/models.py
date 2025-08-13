from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from Department.models import Department

class Course(models.Model):
    courseCode = models.CharField(max_length=10, unique=True)  # e.g., CSE101
    courseName = models.CharField(max_length=100)
    credit = models.DecimalField(max_digits=4, decimal_places=2)  # e.g., 3.00
    department =models.ForeignKey(Department, on_delete=models.CASCADE)
    entryDate = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.courseCode} - {self.courseName}"

    def save(self, *args, **kwargs):
        # Validation
        if not self.courseCode.strip():
            raise ValidationError("Course code cannot be empty")
        if self.credit not in (1.5,3):
            raise ValidationError("credit must be a 1.5 or 3")

        # Formatting
        self.courseCode = self.courseCode.upper()
        self.courseName = self.courseName.title()
        

        super().save(*args, **kwargs)
