from django.urls import path
from .views import *

app_name = 'menstruations'

urlpatterns = [
    path('', root, name='root'),
    path('test_create_menstruation', test_create_menstruation, name='test_create_menstruation'),
    path('create', create_menstruation, name='create_menstruation'),
    path('<int:pk>/update', update_menstruation, name='update_menstruation'),
    path('<int:pk>/delete', delete_menstruation, name='delete_menstruation'),
]