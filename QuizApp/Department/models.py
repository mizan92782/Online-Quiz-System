from django.utils import timezone

from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=100)
    fullForm = models.TextField(max_length=50,blank=True)
    start = models.DateField(default=timezone.now)
    

    def __str__(self):
        return self.title
      
    def save(self,*args, **kwargs):
      self.title= self.title.upper()
      self.fullForm  = self.fullForm.title()
      return super().save()