from django.urls import path
from .views import api_signup, api_login

app_name = 'accounts'

urlpatterns = [
    path('signup/', api_signup, name='signup'),
    path('login/', api_login, name="login"),
]