from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sports(models.Model):
    CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
    ]

    name = models.CharField(max_length= 50, unique= True, verbose_name= _('Name'))
    modality = models.CharField(max_length= 50, choices= CHOICES, verbose_name= _('Modality'))
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Sport')
        verbose_name_plural = _('Sports')
        ordering = ['name']
