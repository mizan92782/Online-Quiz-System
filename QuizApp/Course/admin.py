from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("courseCode", "courseName", "credit", "department", "entryDate")
    search_fields = ("courseCode", "courseName", "department")
    list_filter = ("department",)
