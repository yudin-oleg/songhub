import django_filters
from .models import Song


class SongFilter(django_filters.FilterSet):

    class Meta:
        model = Song
        fields = ['genre']
