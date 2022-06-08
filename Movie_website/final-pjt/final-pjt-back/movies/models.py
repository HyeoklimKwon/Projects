from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movie_genre', blank=True)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    release_date = models.DateField()
    title = models.CharField(max_length=50)
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.CharField(max_length=200)
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
