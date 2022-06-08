from operator import ge
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.TextField()
    release_date = models.DateField()
    genre_choices = (('코미디','코미디'), ('러브코미디','러브코미디'), ('느와르','느와르'))    
    genre = models.CharField(max_length=30, choices= genre_choices)
    score = models.TextField()
    poster_url = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}. {self.title}'
