import openpyxl
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iplclone.settings')
import django
django.setup()
from iplapp.models import *

def bulkinsert1():
    wb = openpyxl.load_workbook('E:\\summer\\summer files\\matches.xlsx')

    ws = wb.active
    flag = 0
    row = 1
    li=[]
    for i in ws:
        if flag==0:
            flag=1
            continue
        if row<1:
            row+=1
            continue
        i1=[]
        for j in i:
            try:
                val = int(j.value)
                i1.append(val)
            except:
                if j.value == None:
                    st = ''
                else:
                    st = j.value
                i1.append(st)
        li.append(Matches(match_id=i1[0],season=i1[1],city=i1[2],date=i1[3],team1=i1[4],
                   team2=i1[5],toss_winner=i1[6],toss_decision=i1[7],
                   result=i1[8],dl_applied=i1[9],winner=i1[10],win_by_runs=i1[11],win_by_wickets=i1[12]
                   ,player_of_match=i1[13],venue=i1[14],umpire1=i1[15],
                    umpire2=i1[16],umpire3=i1[17]))
        row+=1
        if row==757:
            break
    Matches.objects.bulk_create(li)

def bulkinsert():
    wb = openpyxl.load_workbook('E:\\summer\\summer files\\deliveries.xlsx')

    ws = wb.active
    flag = 0
    row = 1
    li=[]
    for i in ws:
        if flag==0:
            flag=1
            continue
        if row<160000:
            row+=1
            continue
        i1=[]
        for j in i:
            try:
                val = int(j.value)
                i1.append(val)
            except:
                if j.value == None:
                    st = ''
                else:
                    st = j.value
                i1.append(st)
        li.append(Delivers(match_id=Matches.objects.get(match_id=i1[0]),inning=i1[1],batting_team=i1[2],bowling_team=i1[3],over=i1[4],
                   ball=i1[5],batsman=i1[6],non_stricker=i1[7],
                   bowler=i1[8],is_super_over=i1[9],wide_runs=i1[10],bye_runs=i1[11],legbye_runs=i1[12]
                   ,noball_runs=i1[13],penality_runs=i1[14],batsman_runs=i1[15],
                    extra_runs=i1[16],total_runs=i1[17],player_dismissed=i1[18],dismissal_kind=i1[19],fielder=i1[20]))
        row+=1
        if row==180000:
            break
    Delivers.objects.bulk_create(li)

if __name__=='__main__':
    bulkinsert()