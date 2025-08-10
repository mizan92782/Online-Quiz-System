from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    Name = models.CharField(max_length=30)       # CharField supports max_length
    UID = models.CharField(max_length=20)
    Department = models.CharField(max_length=50)
    Status = models.CharField(max_length=30)
    Join_Date = models.DateField(default=timezone.now)  # DateField stores date only

    def __str__(self):
        return f"{self.Name} ({self.UID})"
  
    def save(self, *args, **kwargs):
        if self.Name:
            self.Name = self.Name.title()
        if self.Status:
            self.Status = self.Status.title()
        if self.Department:
            self.Department = self.Department.upper()
        if self.UID:
            self.UID = str(self.UID).upper()

        super().save(*args, **kwargs)
