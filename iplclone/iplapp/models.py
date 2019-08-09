from django.db import models

# Create your models here.
class Matches(models.Model):
    match_id=models.IntegerField()
    season=models.IntegerField()
    city=models.CharField(max_length=50,null=True)
    date=models.DateField()
    team1=models.CharField(max_length=80,null=True)
    team2=models.CharField(max_length=70,null=True)
    toss_winner=models.CharField(max_length=70,null=True)
    toss_decision=models.CharField(max_length=30,null=True)
    result=models.CharField(max_length=20,null=True)
    dl_applied=models.IntegerField()
    winner=models.CharField(max_length=70,null=True)
    win_by_runs=models.IntegerField()
    win_by_wickets=models.IntegerField()
    player_of_match=models.CharField(max_length=70,null=True)
    venue=models.CharField(max_length=100,null=True)
    umpire1=models.CharField(max_length=50,null=True)
    umpire2=models.CharField(max_length=50,null=True)
    umpire3=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.match_id

class Delivers(models.Model):
    match_id=models.ForeignKey(Matches,on_delete=models.CASCADE)
    inning=models.IntegerField()
    batting_team=models.CharField(max_length=70,null=True)
    bowling_team=models.CharField(max_length=70,null=True)
    over=models.IntegerField()
    ball=models.IntegerField()
    batsman=models.CharField(max_length=50,null=True)
    non_stricker=models.CharField(max_length=50,null=True)
    bowler=models.CharField(max_length=50,null=True)
    is_super_over=models.BooleanField()
    wide_runs=models.IntegerField()
    bye_runs=models.IntegerField()
    legbye_runs=models.IntegerField()
    noball_runs=models.IntegerField()
    penality_runs=models.IntegerField()
    batsman_runs=models.IntegerField()
    extra_runs=models.IntegerField()
    total_runs=models.IntegerField()
    player_dismissed=models.CharField(max_length=50,null=True)
    dismissal_kind=models.CharField(max_length=30,null=True)
    fielder=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.match_id