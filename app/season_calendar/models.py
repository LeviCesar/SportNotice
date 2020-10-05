from django.db import models
from django.utils.translation import ugettext_lazy as _
from teams.models import Teams


class SeasonCalendar(models.Model):
    date = models.DateTimeField()
    team_1 = models.CharField(max_length= 100, verbose_name= _('Team 1'))
    team_2 = models.CharField(max_length= 100, verbose_name= _('Team 2'))
    
    class Meta:
        verbose_name = _('Season Calendar')
        verbose_name_plural = _('Season Calendar')
        unique_together = ['date', 'team_1', 'team_2']

