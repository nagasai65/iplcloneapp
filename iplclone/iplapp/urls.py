from django.shortcuts import redirect
from django.urls import path
from iplapp.views import *
urlpatterns=[
    path('',lambda request:redirect("season_details",2019),name="home"),
    path('ipl/<int:year>/',Season.as_view(),name="season_details"),
    path('ipl/<int:year>/<int:mid>/',MatchDetail.as_view(),name="match_details"),
    path('ipl/login/',Login.as_view(),name="login"),
    path('ipl/register/',Register.as_view(),name="register"),
    path('ipl/logout/',logout_fun,name="logout")
]