from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse
from django.apps import apps

from .models import Rules

Sports = apps.get_model('sports', model_name= 'Sports')

class RulesHandler(APIView):

    # def post(self, request, sport_id):
    #     try:
    #         sport = Sports.objects.get(pk= sport_id)
    #     except ObjectDoesNotExist:
    #         return JsonResponse({'detail': _('Sport does not exist!')}, status = 404)
        
    #     try:

    def get(self, request, sport_id = None):
        try:
            sport = Sports.objects.get(pk= sport_id)
        except ObjectDoesNotExist:
            return JsonResponse({'detail': _('Sport does not exist!')}, status = 404)

        try: 
            rule = sport.rule_bodies.all()[0]
            return JsonResponse({
                'sport': rule.sport.name,
                'title': rule.title,
                'subtitle': rule.subtitle,
                'author': rule.author,
                'body': [{
                    'topic': body.topic,
                    'text': body.text,
                    'image': get_file_or_image_url(request, body),
                    'image_author': body.image_author,
                    'image_description': body.image_description,
                    'file': get_file_or_image_url, 
                    'url': body.url
                } for body in rule.rule_bodies.all()]
            }, status= 200)
        except AttributeError:
            return JsonResponse({'detail': _('Does not exist any article!')}, stauts = 404)

