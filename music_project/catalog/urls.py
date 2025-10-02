from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.album_list, name='album_list'),
    path('tracks', views.track_list, name='track_list'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_track/', views.add_track, name='add_track'),
    path('analytics/', views.analytics_view, name='analytics'),
]

