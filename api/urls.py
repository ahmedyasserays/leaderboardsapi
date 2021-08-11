from django.urls import path
from .views import get_scores, save_score, create_board, api_overview, update_pass


urlpatterns = [
    path('', api_overview, name="overview"),
    path('create_board/', create_board, name='create-board'),
    path('save_score/', save_score, name='save_score'),
    path('get_scores/<str:board_name>/', get_scores, name='get_scores'),
    path('update_password/', update_pass, name='update_password'),
]
