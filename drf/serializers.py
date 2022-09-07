from songhub.models import Song
from account.models import MyUser
from rest_framework import serializers


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['author', 'name', 'singer', 'upload', 'genre']


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'avatar', 'username', 'is_active', 'is_staff', 'is_admin', 'is_superuser']
