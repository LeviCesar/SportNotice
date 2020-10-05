from django.contrib import admin
from .models import Teams, Players, Collaborators, PositionPlayers, CollaboratorsRole

from nested_admin import NestedStackedInline, NestedModelAdmin


class CollaboratorRoleAdmin(NestedStackedInline):
    fields = ['name']
    model = CollaboratorsRole
    extra = 0

@admin.register(Collaborators)
class CollaboratorAdmin(NestedModelAdmin):
    fields = ['name']
    list_display = ['name']
    search_fields = ['name']
    inlines = [CollaboratorRoleAdmin]

class PositionPlayerAdmin(NestedStackedInline):
    fields = ['name']
    model = PositionPlayers
    extra = 0

@admin.register(Players)
class PlayersAdmin(NestedModelAdmin):
    fields = ['name']
    list_display = ['name']
    search_fields = ['name']
    inlines = [PositionPlayerAdmin]

@admin.register(Teams)
class TeamsAdmin(NestedModelAdmin):
    fields = ['name']
    list_display = ['name']
    search_fields = ['name']