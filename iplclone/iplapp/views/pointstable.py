from django.views import View
from iplapp.models import Matches
from django.shortcuts import render
from django.db.models import *

class PointsTable(View):

    def get(self,request,*args,**kwargs):
        matches = Matches.objects.filter(season=kwargs.get("year")).values('winner').filter(~Q(winner=None)).annotate(count=Count('winner')).order_by('-count')
        seasons=Matches.objects.values_list('season').distinct().order_by('-season')
        no_res_match=Matches.objects.filter(season=kwargs.get("year"),winner=None).values('team1','team2')
        res={}
        for i in no_res_match:
            for j in i.values():
                if j in res:
                    res[j]+=1
                else:
                    res[j]=1
        for match in matches:
            match['count'] += match['count']
            if match['winner'] in res:
                match['count'] += res[match['winner']]

        return render(
            request,
            template_name = "iplapp/points_table.html",
            context={
                'matches':matches,
                'seasons':seasons,
                'year':kwargs.get("year"),
            }
        )

