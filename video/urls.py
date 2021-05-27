from django.urls import path, include
from video import views


urlpatterns = [
    path('', views.indexView, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    ]