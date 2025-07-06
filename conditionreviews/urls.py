from django.urls import path
from .views import create_ConditionReview

app_name = 'conditionreviews'

urlpatterns = [
    path('create/', create_ConditionReview, name="create_ConditionReview"),
    
]