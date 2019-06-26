from django.views import View
from iplapp.models import *
from django.shortcuts import render
from django.db.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class MatchDetail(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        match = Matches.objects.values('team1','team2','toss_winner','toss_decision','winner','player_of_match').filter(match_id=kwargs.get("mid"))
        first_inning = Delivers.objects.values('batting_team','total_runs','player_dismissed','dismissal_kind','fielder','over','ball',).filter(match_id=kwargs.get("mid"))
        toprunners = Delivers.objects.filter(match_id=kwargs.get("mid")).values('batsman','batting_team').annotate(runs_sum=Sum('batsman_runs')).order_by('-runs_sum')[:3]
        topwicketers = Delivers.objects.filter(match_id=kwargs.get("mid")).values('bowler','bowling_team').annotate(count=Count('player_dismissed')).order_by('-count')[:3]
        return render(
            request,
            template_name="iplapp/match_details.html",
            context={
                'match': match,
                'first_inning': first_inning.filter(inning=1),
                'second_inning': first_inning.filter(inning=2),
                'toprunners': toprunners,
                'topwicketers': topwicketers,
                'request':request,
            }
        )