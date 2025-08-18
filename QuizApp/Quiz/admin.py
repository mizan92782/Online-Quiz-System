from django.contrib import admin
from .models import Quiz

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id','course', 'batch', 'teacher','question', 'quiz_no','quiz_marks','start', 'end', 'created_at')
    search_fields = ('course__courseCode', 'batch__Batch', 'teacher__Name')
    list_filter = ('start',)
    readonly_fields=['title','quiz_marks']