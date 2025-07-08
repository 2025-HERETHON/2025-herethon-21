from django.urls import path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('example', example, name='example'),
    path("componentpage", componentpage, name="componentpage"),
    path("cyclepage", cyclepage, name="cyclepage"),
    path("scrappage", scrappage, name="scrappage"),
    path("periodpage", periodpage, name="periodpage"),
    path("componentcalendar", componentcalendar, name="componentcalendar"),
    path("mypage", mypage, name="mypage"),
    path("friendpage", friendpage, name="friendpage"),
    path("restpage", restpage, name="restpage"),
    path("editpage", editpage, name="editpage"),
]