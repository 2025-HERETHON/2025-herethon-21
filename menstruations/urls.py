from django.urls import path
from .views import *

app_name = 'menstruations'

urlpatterns = [
    path('', root, name='root'),
    path('read/create_form', test_create_menstruation, name='read/create_form'),
    path('create', create_menstruation, name='create'),
    path('<int:pk>/update', update_menstruation, name='update'),
    path('<int:pk>/delete', delete_menstruation, name='delete'),
]