from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display=['id','name','UID','department','batch','admission_date']
  readonly_fields=['UID']