from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse

from . import models


class SportsHandler(APIView):

    def post(self, request):
        form = request.data
        try: 
            sport = models.Sports.objects.create(name = form.get('name'))
        except ValidationError:
            return JsonResponse({
                'detail': _('Sport name is required!')
            }, status = 400)
        
        try:
            modality = models.Modalities.objects.get_or_create(
                modality = form.get('modality'),
                sport = sport)
        except ObjectDoesNotExist:
            sport.delete()
            return JsonResponse({
                'detail': _('Modality does not exist!')
            }, status = 404)
        except ValidationError:
            sport.delete()
            return JsonResponse({
                'detail': _('Modality type is required!')
            }, status = 400)

        return JsonResponse({
            'id': sport.id,
            'name': sport.name,
            'modality': modality.modality
        }, status = 201)
    
    def get(self, request):
        sports = models.Sports.objects.all()
        if sports:
            list_content = []
            for sport in sports:
                content = {
                    'id': sport.id,
                    'name': sport.name,
                    'modality': sport.modalities.modality
                }
                list_content.append(content)
            status = 200
        else:
            list_content, status ={
                'detail': _('Sport name is required!')
            }, 400
        return JsonResponse(list_content, status = status)
    
    def put(self, request, sport_id):
        form = request.data
        try:
            sport = models.Sports.objects.get(pk = sport_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Sport does not exist!')
            }, status = 404)
        
        try:
            modality = models.Modalities.objects.get(modality = form.get('modality'))
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Modality does not exist!')
            }, status = 404)
        
        sport.name = form.get('name')
        sport.modalities = modality
        sport.save()

        return JsonResponse({
            'id': sport.id,
            'name': sport.name,
            'modality': modality.modality
        }, status = 200)
    
    def delete(self, request, sport_id):
        try:
            sport = models.Sports.objects.get(pk= sport_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Sport does not exist!')
            }, status = 404)

        sport.delete()
        return JsonResponse({
            'detail': _('Sport delete with success!')
        }, status = 200)    
