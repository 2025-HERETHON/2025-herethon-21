from django.urls import path
from .views import main_view, signup_view, login_view, logout_view, delete_account_view

app_name = 'accounts'

urlpatterns = [
    path('', main_view, name="main"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('delete/', delete_account_view, name="delete_account")
]