from django.shortcuts import render, get_object_or_404, redirect
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
        contents = {'form': AlbumForm(instance=album), 'pk': pk}
        return render(request, 'music/album_detail.html', contents)
    else:
        form = AlbumForm(request.POST)
        form.save()
    return render(request, 'music/edit_album.html', {'form': form})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('post-album-list')
