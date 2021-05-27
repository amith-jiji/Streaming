from django.urls import path, include
from feed import views


urlpatterns = [
    path('', views.indexView, name='index'),
    path('video_feed1', views.video_feed1, name='video_feed1'),
    ]