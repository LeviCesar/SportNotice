from django.contrib import admin
from .models import Sports


@admin.register(Sports)
class SportAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['name', 'modality']
    list_filter = ['modality']
    search_fields = ['name']