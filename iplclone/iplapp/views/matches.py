from django.views import View
from iplapp.models import *
from django.shortcuts import render
from django.db.models import *
from django.contrib.auth.mixins import LoginRequiredMixin



class MatchDetail(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        match = Matches.objects.filter(match_id=kwargs.get("mid")).values()
        inning = Delivers.objects.filter(match_id=Matches.objects.get(match_id=kwargs.get("mid"))).values()
        team1_score = inning.filter(inning=1).aggregate(score=Sum('total_runs'), noofwic=Count('player_dismissed',
                                                                                               filter=~Q(
                                                                                                   player_dismissed='')))
        team2_score = inning.filter(inning=2).aggregate(score=Sum('total_runs'), noofwic=Count('player_dismissed',
                                                                                               filter=~Q(
                                                                                                   player_dismissed='')))
        toprunners =inning.values('batsman', 'batting_team').annotate(runs_sum=Sum('batsman_runs')).order_by('-runs_sum')[:3]
        topwicketers = inning.values('bowler', 'bowling_team').annotate(count=Count('player_dismissed',filter=~Q(player_dismissed=''))).order_by('-count')[:3]


        return render(
            request,
            template_name="iplapp/match_details.html",
            context={
                'match': match,
                'first_inning': inning.filter(inning=1),
                'second_inning': inning.filter(inning=2),
                'toprunners': toprunners,
                'topwicketers': topwicketers,
                'team1_score': team1_score,
                'team2_score': team2_score,
            }
        )