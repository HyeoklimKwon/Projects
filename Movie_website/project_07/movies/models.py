import django
from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    title = models.CharField(max_length=20)    
    description = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name= 'like_movies') 
    
    def __str__(self):
        return f'{self.pk}. {self.title}'

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.content}'