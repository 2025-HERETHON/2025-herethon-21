from django.urls import path
from .views import api_signup

app_name = 'accounts'

urlpatterns = [
    path('signup/', api_signup, name='signup')
]