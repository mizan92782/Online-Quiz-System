from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Batch(models.Model):
    batch = models.IntegerField()
    division = models.CharField(max_length=1)
    title = models.CharField(max_length=10)  # Required max_length
    entryDate = models.DateField(default=timezone.now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.batch} - {self.division}"

    def save(self, *args, **kwargs):
        # Validation
        if len(str(self.batch)) != 2:
            raise ValidationError("Batch must be exactly 2 digits")
        if len(self.division) != 1:
            raise ValidationError("Batch division must be a single character")
        
        # Formatting
        self.division = self.division.upper()
        self.title = f"{self.batch}-{self.division}"
        
        super().save(*args, **kwargs)
