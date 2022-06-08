from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        #전체 게시물
        movies = Movie.objects.order_by('-pk')

        context = {
            'movies' : movies,
        }
        return render(request, 'movies/index.html', context)
    return redirect('accounts:login')

def detail(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk = pk)
        commentform = CommentForm()
        comments = movie.comment_set.all()
        context = {
            'movie' : movie,
            'commentform' : commentform,
            'comments' : comments
        }
        return render(request, 'movies/detail.html', context)
    return redirect('accounts:login')

def create(request):
    if request.user.is_authenticated:
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
    return redirect('accounts:login')

def delete(request, pk):
    if request.user.is_authenticated:
        """
        POST: DB에서 정보 삭제
        """
        movie = get_object_or_404(Movie, pk=pk)
        if request.method == 'POST':
            movie.delete()
            return redirect('movies:index')
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')
    

def update(request, pk):
    if request.user.is_authenticated:
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
    return redirect('accounts:login')


def comments_create(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            movie = get_object_or_404(Movie, pk=pk)
            commentform = CommentForm(request.POST)
            if commentform.is_valid():
                comment = commentform.save(commit=False)
                comment.movie = movie
                comment.save()
            return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')   

@require_POST
def comment_delete(request, movie_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        
        comment.delete()
    return redirect('movies:detail', movie_pk)

def like(request):
    pass