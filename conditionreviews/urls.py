from django.urls import path
from .views import create_ConditionReview, read_ConditionReview, delete_ConditionReview

app_name = 'conditionreviews'

urlpatterns = [
    path('create/', create_ConditionReview, name="create_ConditionReview"),
    path('read/<str:date_str>/', read_ConditionReview, name="read_ConditionReview"),
    path('delete/<str:date_str>/', delete_ConditionReview, name="delete_ConditionReview"),
]