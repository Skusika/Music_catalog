from django.shortcuts import render, redirect
from .forms import TrackForm, AlbumForm
from .models import Track, Album


# Create your views here.

def add_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track_list')
    else:
        form = TrackForm()
    return render(request, 'catalog/add_track.html', {'form': form})


def track_list(request):
    tracks = Track.objects.all().order_by('-created_at')
    return render(request, 'catalog/track_list.html', {'tracks': tracks})


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track_list')  # После добавления — на список треков
    else:
        form = AlbumForm()
    return render(request, 'catalog/add_album.html', {'form': form})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'catalog/album_list.html', {'albums': albums})
