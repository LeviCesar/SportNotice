from django.contrib import admin
from .models import Rules, RuleBodies


class RuleBodiesAdmin(admin.StackedInline):
    model = RuleBodies
    extra = 0

@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    list_disply = ['title', 'author', 'creation_date']
    search_fields = ['title', 'subtitle', 'author', 'creation_date']
    inlines = [RuleBodiesAdmin]