from django.shortcuts import render, get_object_or_404
from .forms import AlbumForm
from .models import Album

# Create your views here.


def post_album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


def add_album(request):
    form = AlbumForm()
    return render(request, 'music/add_album.html', {'form': form})
