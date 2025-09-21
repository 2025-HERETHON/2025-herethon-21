from django.urls import path
from .views import *
from django.shortcuts import redirect

app_name = 'frontend'

urlpatterns = [
    path("", lambda request: redirect("frontend:loginpage"), name="home"),

    path("login", loginpage, name="loginpage"),
    path("signup", signuppage, name="signuppage"),
    path("onboarding_1", onboarding_1, name="onboarding_1"),
    path("onboarding_2", onboarding_2, name="onboarding_2"),
    path("onboarding_3", onboarding_3, name="onboarding_3"),
    path("lastmenstruation", lastmenstruationpage, name="lastmenstruationpage"),
    path("purpose", purposepage, name="purposepage"),

    path("cycle", cyclepage, name="cyclepage"),
    path("rest", restpage, name="restpage"),
    path("scrap", scrappage, name="scrappage"),
    path("period", periodpage, name="periodpage"),
    path("edit", editpage, name="editpage"),
    path("alarm", alarmpage, name="alarmpage"),
    
    path("routineing", routineingpage, name="routineingpage"),
    path("finishedroutine", finishedroutine, name="finishedroutine"),

    path("mypagemain", mypagemain, name="mypagemain"),
    path("friend/<str:friend_username>", friendpage, name="friendpage"),

    path("makefriends", makefriends, name="makefriends"),
    path('friendsconfirm/<str:email>/', friendsconfirm, name='friendsconfirm'),
    path("friended/", friended, name="friended"),
]

