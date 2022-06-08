from django.shortcuts import render
from django.views.decorators.http import require_safe
from  .models import Genre, Movie
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': page_obj,
    }
    return render(request,'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    genres = movie.genres.all()
    context = {
        'movie' : movie,
        'genres' : genres,
    }
    return render(request, 'movies/detail.html', context)



@require_safe
def recommended(request):
    
    movies = Movie.objects.filter(genres = 12)
    context = {
        'movies' : movies
    }     
    return render(request, 'movies/recommended.html', context)

def todetail(request, genre_pk):

    movies = Movie.objects.filter(genres = genre_pk)
    context = {
        'movies' : movies
    }
    return render(request, 'movies/todetail.html', context)
    


