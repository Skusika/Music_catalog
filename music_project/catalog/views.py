from django.shortcuts import render, redirect
from .forms import TrackForm, AlbumForm
from .models import Track, Album, Artist
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64



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


def analytics_view(request):
    #Загружаем все данные
    albums = Album.objects.all().values('id', 'title', 'artist')
    tracks = Track.objects.all().values('id', 'title', 'genre', 'album')
    artists = Artist.objects.all().values('id', 'name')

    # Превращаем в DataFrame
    df_albums = pd.DataFrame(albums)
    df_tracks = pd.DataFrame(tracks)
    df_artists = pd.DataFrame(artists)

    # Аналитика
    albums_per_artist = df_albums.groupby('artist')['title'].count().reset_index()
    avg_tracks_per_album = df_tracks.groupby('album')['title'].count().mean()

    # context = {
    #     'albums_per_artist': albums_per_artist.to_dict(orient='records'),
    #     'avg_tracks_per_album': round(avg_tracks_per_album, 2),
    # }
    # return render(request, 'catalog/analytics.html', context)
    # График
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(albums_per_artist['artist'], albums_per_artist['title'], color='skyblue')
    ax.set_xlabel("Исполнитель")
    ax.set_ylabel("Кол-во альбомов")
    ax.set_title("Альбомы по исполнителям")
    plt.xticks(rotation=45, ha='right')

    # Сохраняем график в буфер
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    context = {
        'albums_per_artist': albums_per_artist.to_dict(orient='records'),
        'avg_tracks_per_album': round(avg_tracks_per_album, 2),
        'chart': image_base64
    }
    return render(request, 'catalog/analytics.html', context)
