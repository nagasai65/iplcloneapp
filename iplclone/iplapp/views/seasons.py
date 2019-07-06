from iplapp.models import *
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.db.models import *

# class Season(View):
#
#     def get(self, request, *args, **kwargs):
#         matches=Matches.objects.values('match_id','team1','team2','venue','toss_winner','toss_decision','result','player_of_match').filter(season=kwargs.get("year"))
#         seasons=Matches.objects.values_list('season').order_by('-season').distinct()
#         return render(
#             request,
#             template_name='iplapp/seasons.html',
#             context={
#                 'matches':matches,
#                 'seasons_list':seasons,
#                 'year':kwargs.get("year"),
#             }
#         )
#

class Season(View):

    def get(self,request,*args,**kwargs):
        matches_list=Matches.objects.values('match_id','team1','team2','venue','toss_winner','toss_decision','result','player_of_match').filter(season=kwargs.get("year"))
        seasons_list=Matches.objects.values_list('season').order_by('-season').distinct()
        paginator=Paginator(matches_list,8)
        page=request.GET.get('page')
        matches=paginator.get_page(page)
        return render(
            request,
            'iplapp/seasons.html',
            {'matches': matches,
             'seasons_list': seasons_list,
             'year': kwargs.get("year"),
             }
        )

