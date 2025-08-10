from django.db import models
from django.forms import ValidationError
from django.utils import timezone

# Create your models here.

class Student(models.Model):
  Name=models.CharField(max_length=30)
  UID = models.IntegerField(unique=True)
  Department = models.CharField(max_length=10)
  Batch = models.CharField(max_length=3)
  Admission_Date = models.DateField(default=timezone.now)
  
  def __str__(self):
    return f"{0}+ {1}".format(self.Name,self.Batch)
  

  def save(self,*args, **kwargs):
    if len(self.UID) != 8:
      raise ValidationError("UID must be exactly  8 characters")
  
    self.Name=self.Name.title()
    self.Department=self.Department.upper()
    self.UID = self.Department+" "+self.UID;
    self.Batch=self.Batch.upper()
  
    return super().save()