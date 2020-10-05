from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from sports.models import Sports


class Rules(models.Model):
    sport = models.ForeignKey(
        to= Sports, on_delete= models.CASCADE, related_name= 'rules')
    title = models.CharField(max_length= 50, verbose_name= _('Title'))
    subtitle = models.TextField(blank= True, verbose_name= _('Subtitle'))
    author = models.CharField(max_length= 100, verbose_name= _('Author'))
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('Rule')
        verbose_name_plural = _('Rules')
    
    @classmethod
    def create_article(cls, sport, title, subtitle, author,
        creation_date, update_date, body):
        try:
            article = cls.objects.create(
                sport = sport, 
                title = title, 
                subtitle = subtitle, 
                author = author,
                createion_date = creation_date, 
                update_date = update_date
            )
            return {
                'sport': article.sport.name,
                'title': article.title,
                'subtitle': article.subtitle,
                'author': article.author
            }, 201
        except ValidationError:
            return _('Missing fields is necessary to create an article!'), 400
        except IntegrityError:
            return _('Article already exist!'), 409

class RuleBodies(models.Model): #RuleBody
    rule = models.ForeignKey(
        to= Rules, on_delete= models.CASCADE, related_name= 'rule_bodies')
    topic = models.CharField(max_length= 100, blank= True, verbose_name= _('Topic'))
    text = models.TextField(blank= True, verbose_name= _('Text'))
    image = models.ImageField(blank= True, verbose_name= _('Image'))
    image_author = models.CharField(max_length= 100, verbose_name= _('Image Author'))
    image_description = models.CharField(max_length= 150, verbose_name= _('Image Description'))
    file = models.FileField(blank= True , verbose_name= _('File attachment'))
    url = models.CharField(max_length= 150, blank= True, verbose_name= 'Link')  
    
    class Meta:
        verbose_name = _('Rule Body')
        verbose_name_plural = _('Rule Bodies')
    
    @classmethod
    def create_article_body(cls, request, rule, body):
        try:
            list_response = []
            for section in body:
                body = cls.objects.create(**section, rule= rule)
                content = {
                    'topic': body.topic,
                    'text': body.text,
                    'image': body.image.url,
                    'image_author': body.image_author,
                    'image_description': body.image_description,
                    'file': body.file.url, 
                    'url': body.url
                }
                list_response.append(content)
            return list_response, 201
        except:
            return _('There was an error creating the rule body!'), 400 
