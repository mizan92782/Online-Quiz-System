from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'uid','password', 'department','password','status', 'join_date']

    search_fields = ['uid']
    readonly_fields=['uid']
