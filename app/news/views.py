from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse

from datetime import datetime, timedelta
from django.apps import apps
from . import models

Sports = apps.get_model('sports', model_name='Sports')

class ArticlesHandler(APIView):

    # def post(slef, request, sport_id):
    #     """
    #     {
    #         sport_id: int,
    #         title: str,
    #         subtitle: str(optional),
    #         author: str,
    #         body:[
    #             {
    #                 topic: str(optional),
    #                 text: str(optional),
    #                 image: str(optional),
    #                 image_author: str(if have image is required else not required),
    #                 image_description: str(if have image is required else not required),
    #                 file = file(option),
    #                 url: str
    #             },
    #             {
    #                 topic: str(optional),
    #                 text: str(optional),
    #                 image: image(optional),
    #                 image_author: str(if have image is required else not required),
    #                 image_description: str(if have image is required else not required),
    #                 file = file(option),
    #                 url: str
    #             }
    #         ]
    #     }
    #     """
    #     form = request.data
    #     try:
    #         sport = Sports.objects.get(pk = sport_id)
    #     except ObjectDoesNotExist:
    #         return JsonResponse({
    #             'detail': _('Sport does not exist!')
    #         }, status = 404)
        
    #     body = form.pop('body')
    #     response, status = models.Article.create_article(**form)
    #     if article:
    #         body, status = models.ArticleBody.create_article_body(request, response, body)
    #         if body:
    #             response['body'] = body
    #             return JsonResponse(response, status = status)
    #         else:
    #             response = body
        
    #     return JsonResponse({
    #         'detail': response
    #     }, status = status)
    
    def get(self, request, sport_id = None):
        articles = models.Article.objects.all()
        if articles:
            x = 10
            if sport_id:
                while True:
                    date_start = datetime.now() - timedelta(days= x)
                    date_now = datetime.now() - timedelta(days= x-10)
                    articles = models.Article.objects.filter(
                        creation_date__range = [date_start, date_now], sport_id = sport_id)
                    if not articles:
                        x+=10
            else:
                while True:
                    date_start = datetime.now() - timedelta(days= x)
                    date_now = datetime.now() - timedelta(days= x-10)
                    articles = models.Article.objects.filter(
                        creation_date__range = [date_start, date_now])
                    if not articles:
                        x+=10
            
            return JsonResponse([{
                'sport': article.sport.name,
                'title': article.title,
                'subtitle': article.subtitle,
                'author': article.author,
                'body': [{
                    'topic': body.topic,
                    'text': body.text,
                    'image': get_file_or_image_url(request, body),
                    'image_author': body.image_author,
                    'image_description': body.image_description,
                    'file': get_file_or_image_url, 
                    'url': body.url
                } for body in article.article_bodies.all()]
            } for article in articles], status= 200, safe= False)
        else:
            return JsonResponse({'detail': _('Does not exist any article!')}, stauts = 404)

    def delete(self, request, article_id):
        try:
            article = models.Article.objects.get(pk = article_id)
            article.delete()
            return JsonResponse({'detail': _('Article deleted with success!')}, status = 200)
        except ObjectDoesNotExist:
            return JsonResponse({'detail': _("It's not possible delete this article because it not exist!")}, status = 404)
            
