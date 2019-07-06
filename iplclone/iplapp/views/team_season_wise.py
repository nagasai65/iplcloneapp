from django.views import View
from django.db.models import *
from iplapp.models import *
from django.shortcuts import *


class TeamSeasonWise(View):

    def get(self, request, *args, **kwargs):

        if kwargs.get("year") == 2019 and kwargs.get("team") == "Delhi Daredevils":
            kwargs["team"] = "Delhi Capitals"
        matches = Matches.objects.filter(season=kwargs.get("year")).filter(Q(team1=kwargs.get("team")) | Q(team2=kwargs.get("team")))
        matches=matches.values('team1','team2','win_by_wickets','win_by_runs','venue','city','match_id','season','winner').annotate(
            score1=Sum('delivers__total_runs',filter=Q(delivers__inning=1)),
            score2=Sum('delivers__total_runs',filter=Q(delivers__inning=2)),
            wic1=Count('delivers__player_dismissed',filter=~Q(delivers__dismissal_kind=None) & Q(delivers__inning=1)),
            wic2=Count('delivers__player_dismissed',filter=~Q(delivers__player_dismissed=None) & Q(delivers__inning=2))
        )
        return render(
            request,
            template_name="iplapp/team_season_wise.html",
            context={
                'team': kwargs.get("team"),
                'matches': matches,
            }
        )