from django.contrib import admin
from .models import Batch

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("batch", "division", "title", "entryDate", "complete")
    search_fields = ("batch", "division", "title")
    list_filter = ("complete", "division")
    readonly_fields=['title']
