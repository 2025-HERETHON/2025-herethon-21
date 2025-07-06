from django.urls import path
from .views import create_ConditionReview, read_ConditionReview

app_name = 'conditionreviews'

urlpatterns = [
    path('create/', create_ConditionReview, name="create_ConditionReview"),
    path('read/<str:date_str>/', read_ConditionReview, name="read_ConditionReview")
]