from django.shortcuts import render
from songhub.models import Song
from account.models import MyUser
from rest_framework import viewsets, permissions
from drf.serializers import SongSerializer, MyUserSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [permissions.IsAuthenticated]
