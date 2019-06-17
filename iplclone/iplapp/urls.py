from django.shortcuts import redirect
from django.urls import path
from iplapp.views import *
urlpatterns=[
    path('',lambda request:redirect("season_details",2019)),
    path('ipl/<int:year>/',Season.as_view(),name="season_details")
]