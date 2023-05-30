from django import forms
from .models import Album, Image


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'artist', 'year', 'label', 'is_active')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image', 'album')
