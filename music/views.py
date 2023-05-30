from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumForm, ImageForm
from .models import Album, Artist, Image


# Create your views here.


def post_album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        form.save()
        return redirect('post-album-list')
    return render(request, 'music/add_album.html', {'form': form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album-detail', pk=pk)
    return render(request, 'music/edit_album.html', {'form': form})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('post-album-list')


def albums_by_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    albums = Album.objects.filter(artist_id=pk)
    context = {
        'artist': artist,
        'albums': albums,
    }
    return render(request, 'music/albums_by_artist.html', context)


def image_by_album(request, pk):
    image = get_object_or_404(Image, pk=pk)
    albums = Album.objects.filter(album_id=pk)
    context = {
        'image': image,
        'albums': albums,
    }
    return render(request, 'music/index.html', context)


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'music/add_image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'music/add_image.html', {'form': form})
