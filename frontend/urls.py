from django.urls import path
from .views import *
from django.shortcuts import redirect


app_name = 'frontend'

urlpatterns = [
    path("", lambda request: redirect("frontend:loginpage"), name="home"),
    path("onboarding_1", onboarding_1, name="onboarding_1"),
    path("onboarding_2", onboarding_2, name="onboarding_2"),
    path("onboarding_3", onboarding_3, name="onboarding_3"),
    path("signuppage", signuppage, name="signuppage"),
    path("componentpage", componentpage, name="componentpage"),
    path("cyclepage", cyclepage, name="cyclepage"),
    path("scrappage", scrappage, name="scrappage"),
    path("periodpage", periodpage, name="periodpage"),
    path("componentcalendar", componentcalendar, name="componentcalendar"),
    path("componentcalendar", componentcalendar, name="componentcalendar"),
    path("mypage", mypage, name="mypage"),
    path("friendpage", friendpage, name="friendpage"),
    path("restpage", restpage, name="restpage"),
    path("editpage", editpage, name="editpage"),
]