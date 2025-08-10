from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','Name', 'UID', 'Department', 'Status', 'Join_Date']

    search_fields = ['UID']
