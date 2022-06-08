from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.TextField()
    poster_url = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}. {self.title}'
