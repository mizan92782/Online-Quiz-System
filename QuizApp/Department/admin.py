from django.contrib import admin

from .models import Department

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
  '''Admin View for Department'''

  list_display = ['id','title','start']
  
