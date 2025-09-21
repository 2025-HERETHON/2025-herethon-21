from django.urls import path
from .views import *

app_name = 'menstruations'

urlpatterns = [
    path('create', create_menstruation, name='create'),
    path('<int:pk>/update', update_menstruation, name='update'),
    path('<int:pk>/delete', delete_menstruation, name='delete'),
]