from django.urls import include, path
from rest_framework import routers
from drf import views

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)
router.register(r'users', views.MyUserViewSet)
