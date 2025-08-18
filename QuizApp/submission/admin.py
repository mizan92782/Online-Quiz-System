from django.contrib import admin
from submission.models import Submission

# Register your models here.
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
  list_display=['id','quiz','student','marks']
  