from django.urls import path
from .views import main, login, logout, signup

app_name = "KakaoAPI"

urlpatterns = [
    path('', main, name="main"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
]
