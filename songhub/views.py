from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Song, GENRES
from django.contrib.auth.models import User
from .forms import SongForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .filters import SongFilter

User = get_user_model()


class Filter:

    def __init__(self, model, fields):
        pass


def song_list(request):
    #songs = Song.objects.order_by('name')
    #songs = Song.objects.order_by('duration')
    #songs = sorted(Song.objects.all(), key=lambda x: x.get_duration())
    f = SongFilter(request.GET, queryset=Song.objects.all())
    paginator = Paginator(f.qs, 4)
    page_number = request.GET.get('page')
    songs_page = paginator.get_page(page_number)
    return render(request, 'songhub/song_list.html', {'songs_page': songs_page, 'GENRES': GENRES})


def user_profile(request, pk):
    if not User.objects.filter(pk=pk).exists():
        raise Http404('User does not exist')
    #songs = Song.objects.filter(author__pk=pk).order_by('created_date')
    f = SongFilter(request.GET, queryset=Song.objects.filter(author__pk=pk))
    paginator = Paginator(f.qs, 4)
    page_number = request.GET.get('page')
    songs_page = paginator.get_page(page_number)
    return render(request, 'songhub/user_profile.html', {'songs_page': songs_page, 'GENRES': GENRES})


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.save()
            return redirect('user_profile', request.user.pk)
    else:
        form = SongForm()
    return render(request, 'songhub/add_song.html', {'form': form})


def delete_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.delete()
    return redirect('user_profile', request.user.pk)
