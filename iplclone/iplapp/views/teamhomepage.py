from django.views import View
from django.shortcuts import render
from iplapp.models import *
from django.db.models import Q, Sum, Count,F,Max


class Teamspage(View):

    def get(self, request):

        return render(
            request,
            template_name="iplapp/teams_page.html",
        )


class TeamHomepage(View):
    def get(self, request, *args, **kwargs):
        matches = Matches.objects.values('season').annotate(
            noof_matches_played=Count('team1',filter=(Q(team1=kwargs.get("team"))|Q(team2=kwargs.get("team")))),
            noof_teams=Count('team1',distinct=True),
            final_match_id=Max('match_id')
        ).order_by('-season')
        return render(
            request,
            template_name="iplapp/team_homepage.html",
            context={
                'matches': matches,
                'team': kwargs.get('team'),
            }
        )