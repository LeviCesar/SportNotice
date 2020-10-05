from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from sports.models import Sports


def get_file_or_image_url(request, obj):
    return ''

class Article(models.Model):
    sport = models.ForeignKey(
        to= Sports, on_delete= models.CASCADE, related_name= 'articles')
    title = models.CharField(max_length= 200, verbose_name= _('Title'))
    subtitle = models.TextField(blank= True, verbose_name= _('Subtitle'))
    author = models.CharField(max_length= 100, verbose_name= _('Author'))
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

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


class ArticleBody(models.Model):
    article = models.ForeignKey(
        to= Article, on_delete= models.CASCADE, related_name= 'article_bodies')
    topic = models.CharField(max_length= 100, blank= True, verbose_name= _('Topic'))
    text = models.TextField(blank= True, verbose_name= _('Text'))
    image = models.ImageField(blank= True, verbose_name= _('Image'))
    image_author = models.CharField(max_length= 100, verbose_name= _('Image Author'))
    image_description = models.CharField(max_length= 150, verbose_name= _('Image Description'))
    file = models.FileField(blank= True , verbose_name= _('File attachment'))
    url = models.CharField(max_length= 150, blank= True, verbose_name= 'Link')  
    
    class Meta:
        verbose_name = _('Body')
        verbose_name_plural = _('Bodies')
    
    @classmethod
    def create_article_body(cls, request, article, body):
        try:
            list_response = []
            for section in body:
                body = cls.objects.create(**section, article= article)
                content = {
                    'topic': body.topic,
                    'text': body.text,
                    'image': body.image.url,
                    'image_author': body.image_author,
                    'image_description': body.image_description,
                    'file': body.file.url, #-> procurar um metodo de retornar a url direto
                    'url': body.url
                }
                list_response.append(content)
            return list_response, 201
        except:
            article.delete()
            return _('There was an error creating the article body!'), 400 
