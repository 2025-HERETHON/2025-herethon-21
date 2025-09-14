from django.urls import path
from .views import *
from django.shortcuts import redirect

app_name = 'frontend'

urlpatterns = [
    path("", lambda request: redirect("frontend:loginpage"), name="home"),

    path("loginpage", loginpage, name="loginpage"),
    path("signuppage", signuppage, name="signuppage"),
    path("onboarding_1", onboarding_1, name="onboarding_1"),
    path("onboarding_2", onboarding_2, name="onboarding_2"),
    path("onboarding_3", onboarding_3, name="onboarding_3"),
    path("lastmenstruationpage", lastmenstruationpage, name="lastmenstruationpage"),
    path("purposepage", purposepage, name="purposepage"),

    path("cyclepage", cyclepage, name="cyclepage"),
    path("restpage", restpage, name="restpage"),
    path("scrappage", scrappage, name="scrappage"),
    path("periodpage", periodpage, name="periodpage"),
    path("editpage", editpage, name="editpage"),
    path("alarmpage", alarmpage, name="alarmpage"),
    
    path("routineingpage", routineingpage, name="routineingpage"),
    path("finishedroutine", finishedroutine, name="finishedroutine"),

    path("mypagemain", mypagemain, name="mypagemain"),
    path("friendpage/<str:friend_id>", friendpage, name="friendpage"),

    path("makefriends", makefriends, name="makefriends"),
    path('friendsconfirm/<str:email>/', friendsconfirm, name='friendsconfirm'),
    path("friended/", friended, name="friended"),
]
