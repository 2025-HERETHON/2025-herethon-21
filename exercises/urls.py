from django.urls import path
from .views import *

app_name = 'exercises'

urlpatterns = [
    path('test', test, name='test'),
    path('test/exercise/start', test_exercise_start, name='test_exercise_start'),
    path('test/exercise/end', test_exercise_end, name='test_exercise_end'),
    path('scrap/create', create_scrapped_exercise_routine, name='scrapped_exercise_routine_create'),
    path('scrap/<str:scrapped_at>/delete', delete_scrapped_exercise_routine, name='scrapped_exercise_routine_delete'),
    path('history/create', create_exercise_history, name='exercise_history_create'),
    path('review/create', create_exercise_review, name='exercise_review_create'),
    path('review/<int:pk>/update', update_exercise_review, name='exercise_review_update'),
    path('review/<int:pk>/delete', delete_exercise_review, name='exercise_review_delete'),
    path('review/<int:exercise_review_id>/reaction/create-or-delete', createordelete_reacted_exercise_review, name='reacted_exercise_review_create_or_delete'),
]