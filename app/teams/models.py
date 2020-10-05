from django.db import models
from django.utils.translation import ugettext_lazy as _
from sports.models import Sports


class Teams(models.Model):
    sport = models.ForeignKey(
        to= Sports, on_delete= models.CASCADE, related_name= 'teams')
    name = models.CharField(max_length= 100, verbose_name= _('Name'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

class Players(models.Model):
    team = models.ForeignKey(
        to= Teams, on_delete= models.CASCADE, related_name= 'players')
    name = models.CharField(max_length= 100, verbose_name= _('Name'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')

class PositionPlayers(models.Model):
    name = models.CharField(max_length= 50, verbose_name= _('Name'))
    player = models.ForeignKey(
        to= Players, on_delete= models.CASCADE, related_name= 'position')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Position Player')
        verbose_name_plural = _('Position Players')


class Collaborators(models.Model):
    team = models.ForeignKey(
        to= Teams, on_delete= models.CASCADE, related_name= 'collaborators')
    name = models.CharField(max_length= 100, verbose_name= _('Name'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('collaborator')
        verbose_name_plural = _('collaborators')

class CollaboratorsRole(models.Model):
    name = models.CharField(max_length= 50, verbose_name= _('Name'))
    collaborator = models.ForeignKey(
        to= Collaborators, on_delete= models.CASCADE, related_name= 'role')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Collaborator Role')
        verbose_name_plural = _('Collaborator Roles')