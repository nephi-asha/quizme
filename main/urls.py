from django.urls import path, include
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name="index"),
    path('play/', views.play, name="play"),
    path('game/', views.game, name="game"),
    path('game/end/', views.end, name="end"),
    path('highscores/', views.highscores, name="highscores"),
    path('api/', include('main.api.urls')),
]
