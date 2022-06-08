from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie()
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description  
    movie.save()

    return redirect('movies:index')

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk= movie_pk)

    # 2. 삭제
    movie.delete()

    return redirect('movies:index')

def edit(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/edit.html', context)

def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
       
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description  
    movie.save()
       
    return redirect('movies:detail', movie.pk)

