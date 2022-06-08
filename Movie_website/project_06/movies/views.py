from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.

def index(request):
    #전체 게시물
    movies = Movie.objects.order_by('-pk')

    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = get_object_or_404(Movie, pk = pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        # form instance <= form class
        form = MovieForm()
    # POST 쪽에서도 활용할 수 있도록
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)

def delete(request, pk):
    """
    POST: DB에서 정보 삭제
    """
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk)

def update(request, pk):
    
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        request.POST
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        
        form = MovieForm(instance = movie)

    context = {
        'movie' : movie,
        'form': form
    }
    return render(request, 'movies/update.html', context)