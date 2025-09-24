from django import forms
from .models import Track, Album


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'album', 'genre']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_date']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_date']
