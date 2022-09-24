from django.shortcuts import render, redirect
from .models import Artist, Song

from .forms import ArtistForm, SongForm
# Create your views here.

# Full CRUD

# GET
def artist_list(request):
    # goes into the database
    artists = Artist.objects.all()
    # returns artists and template 'tunr/artist_list.html'
    return render(request, 'tunr/artist_list.html', {'artists': artists})

# GET
def song_list(request):
    # goes into the database
    songs = Song.objects.all()
    # returns artists and template 'tunr/artist_list.html'
    return render(request, 'tunr/song_list.html', {'songs': songs})

# SHOW
def artist_detail(request, pk):
    # pk stands for primary key
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})

# SHOW
def song_detail(request, pk):
    # pk stands for primary key
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})

# CREATE
def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'tunr/song_form.html', {'form': form})    

# EDIT
def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})

def song_edit(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=artist.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'tunr/song_form.html', {'form': form})

# DELETE
def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')

def song_delete(request, pk):
    Song.objects.get(id=pk).delete()
    return redirect('song_list')
