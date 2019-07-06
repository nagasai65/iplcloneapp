from django import template
from iplapp.models import Matches
from django.utils.safestring import mark_safe

register=template.Library()


@register.filter(name="sub")
def sub(var1,var2):
    return var1-var2


@register.filter(name="getSeasonInfo")
def getSeasonInfo(match,team):
    if match['noof_matches_played'] == (match['noof_teams']-1)*2:
        return mark_safe("<font color='#7F8C8D'>Lost in Leagues</font>")
    else:
        matches = Matches.objects.filter(match_id=match['final_match_id']).values('team1','team2','winner')
        if matches[0]['winner'] == team :
            return mark_safe("<font color='#F1C40F'>Champion</font>")
        elif matches[0]['team1'] == team or matches[0]['team2'] == team:
            return mark_safe("<font color='#DC7633'>Runner</font>")
        else:
            return mark_safe("<font color='#5DADE2'>Reached Play offs</font>")
