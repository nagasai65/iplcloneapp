from iplapp.models import *
from django.shortcuts import render
from django.views import View

class Season(View):

    def get(self, request, *args, **kwargs):
        matches=Matches.objects.values('team1','team2','venue','toss_winner','toss_decision','result','player_of_match').filter(season=kwargs.get("year"))
        seasons=Matches.objects.values_list('season').order_by('-season').distinct()
        return render(
            request,
            template_name='iplapp/seasons.html',
            context={
                'matches':matches,
                'seasons_list':seasons,
                'year':kwargs.get("year"),
            }
        )
