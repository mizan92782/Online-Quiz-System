import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from Batch.models import Batch
from Department.models import Department

class Student(models.Model):
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    UID = models.CharField(max_length=100, unique=True)
    admission_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.batch}"

    def save(self, *args, **kwargs):
        # Formatname
        self.name = self.name.title()
        # Generate UID: Department.Title + batch number + roll
        studentobj= Student.objects.count()+1
        from datetime import datetime

        self.UID = f"{self.department} {datetime.now().year}{self.batch.batch}{studentobj}"

        print(self.UID)

        super().save(*args, **kwargs)
