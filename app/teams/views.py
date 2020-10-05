from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse

from django.apps import apps
from . import models

Sport = apps.get_model('sports', model_name='Sports')


class TeamHandler(APIView):

    def post(self, request):
        # add a team
        """
        requests
        {
            sport_id
        }
        """
        form = request.data 
        try:
            sport = Sport.objects.get(pk= form.get('sport_id'))
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('This sport does not exist!')
            }, status= 404)

        try:
            team = models.Teams.objects.create(**form)
        except ValidationError:
            return JsonResponse({
                'detail': _('All data fields is required!')
            }, status= 400)
        
        return JsonResponse({
            'team_id': team.id,
            'name': team.name,
            'sport': sport.name
        }, status = 201)

    def get(self, request):
        teams = models.Teams.objects.all()
        if teams:
            list_content = []
            for team in teams:
                content = {
                    'team_id': team.id,
                    'name': team.name,
                    'sport': team.sport.name
                }
                list_content.append(content)
            status = 200
        else:
            list_content, status = {
                'detail': _('Teams does not exist!')
            }, 404
        return JsonResponse(list_content, status = status)
    
    def put(self, request, id):
        """
        change a tema
        """
        form = request.data
        try:
            sport = Sport.objects.get(pk= form.get('sport_id'))
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('This sport does not exist!')
            }, status= 404)
        
        try:
            team = models.Teams.objects.get(pk = id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)
        
        team.sport = sport
        team.name = form.get('id')
        team.save()
        
        return JsonResponse({
            'team_id': team.id,
            'name': team.name,
            'sport': team.sport.name
        }, status = 200)
    
    def delete(self, request, id):
        """
        delete a team
        """
        try:
            team = models.Teams.objects.get(pk = id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)
        team.delete()

        return JsonResponse({
            'detail': _('Team delete with success!')
        }, status = 200)


class PlayerHandler(APIView):

    def post(self, request, team_id):
        """
        create player to make 
        {
            position
            name
        }
        """
        form = request.data
        try:
            team = models.Teams.objects.get(pk = team_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)

        try:
            position = models.Positions.objects.get_or_create(**form.pop('position'))
            player = models.Players.objects.create(**form, 
                position= position, team = team)
        except ValidationError:
            return JsonResponse({
                'detail': _('All data fields is required!')
            }, status = 400)
        
        return JsonResponse({
            'team': team.name,
            'name': player.name,
            'position': position.name
        }, status = 201)
    
    def get(self, request, team_id):
        try:
            team = models.Teams.objects.get(pk = team_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)
        
        players = team.players.all()
        if players:
            list_content = []
            for player in players:
                content = {
                    'team': team.name,
                    'name': player.name,
                    'position': player.position.name
                }
                list_content.append(content)
            status = 200
        else:
            list_content, status = {
                'detail': _('Player does not exist!')
            }, 404
        return JsonResponse(list_content, status = status)
    
    def put(self, request, team_id):
        """
        {
            name
            position
        }
        """
        form = request.data
        try:
            team = models.Teams.objects.get(pk = team_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)
        
        try:
            player = team.players.get(name = form.get('name'))
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Player does not exist!')
            }, status = 404)

        try:
            position = player.position.get(name = form.get('position'))
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Position does not exist!')
            }, status = 404)
        
        player.team = team
        player.name = form.get('name')
        player.position = position
        player.save()

        return JsonResponse({
            'team': team.name,
            'name': player.name,
            'position': position.name
        }, status = 200)

    def delete(self, request, player_id):
        try:
            player = models.Players.objects.get(name = player_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Player does not exist!')
            }, status = 404)
        player.delete()
        
        return JsonResponse({
            'detail': _('Player delete with success!')
        }, status = 200)

class Collaborator(APIView):

    def post(self, request, team_id):
        """
        create player to make 
        {
            position
            name
        }
        """
        form = request.data
        try:
            team = models.Teams.objects.get(pk = team_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)

        try:
            position = models.Positions.objects.get_or_create(**form.pop('position'))
            collaborator = models.Collaborators.objects.create(**form, 
                position= position, team = team)
        except ValidationError:
            return JsonResponse({
                'detail': _('All data fields is required!')
            }, status = 400)
        
        return JsonResponse({
            'team': team.name,
            'name': collaborator.name,
            'position': position.name
        }, status = 201)
    
    def get(self, request, team_id):
        try:
            team = models.Teams.objects.get(pk = team_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)
        
        collaborators = team.collaborators.all()
        if collaborators:
            list_content = []
            for collaborator in collaborators:
                content = {
                    'team': team.name,
                    'name': collaborator.name,
                    'position': collaborator.position.name
                }
                list_content.append(content)
            status = 200
        else:
            list_content, status = {
                'detail': _('Collaborator does not exist!')
            }, 404
        return JsonResponse(list_content, status = status)
    
    def put(self, request, team_id):
        """
        {
            name
            position
        }
        """
        form = request.data
        try:
            team = models.Teams.objects.get(pk = team_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Team does not exist!')
            }, status = 404)
        
        try:
            collaborator = team.collaborator.get(name = form.get('name'))
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Collaborator does not exist!')
            }, status = 404)

        try:
            position = collaborator.position.get(name = form.get('position'))
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Position does not exist!')
            }, status = 404)
        
        collaborator.team = team
        collaborator.name = form.get('name')
        collaborator.position = position
        collaborator.save()

        return JsonResponse({
            'team': team.name,
            'name': collaborator.name,
            'position': position.name
        }, status = 200)

    def delete(self, request, collaborator_id):
        try:
            collaborator = models.Collaborators.objects.get(name = collaborator_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'detail': _('Collaborator does not exist!')
            }, status = 404)
        collaborator.delete()
        
        return JsonResponse({
            'detail': _('Collaborator delete with success!')
        }, status = 200)
