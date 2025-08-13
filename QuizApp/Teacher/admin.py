from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'UID', 'department','password','status', 'join_date']

    search_fields = ['UID']
    readonly_fields=['UID','password']
