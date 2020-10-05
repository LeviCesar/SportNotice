from django.contrib import admin
from .models import SeasonCalendar


@admin.register(SeasonCalendar)
class SeasonCalendarAdmin(admin.ModelAdmin):
    fields = ['team_1', 'tam_2']
    list_display = ['team_1', 'team_2']
    search_fields = ['team_1', 'team_2']

