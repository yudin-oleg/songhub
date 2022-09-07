from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('addsong/', views.add_song, name='add_song'),
    path('delete/<int:pk>/', views.delete_song, name='delete_song'),
]