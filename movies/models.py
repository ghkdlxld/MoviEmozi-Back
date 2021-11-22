from django.db import models
from django.conf import settings
from django.db.models.fields import BLANK_CHOICE_DASH, CharField

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    release_date = models.DateField(blank=True)
    poster_path = models.TextField(blank=True)
    popularity = models.FloatField()
    video_id = models.CharField(max_length=500)
    genres = models.CharField(max_length=100, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    runtime = models.CharField(max_length=50)
    backdrop_path = models.TextField(blank=True)
    status= models.TextField(blank=True)
    vote_average = models.FloatField(default=0)
    vote_count = models.IntegerField(default=0)
    adult = models.TextField(blank=True)

    def __str__(self):
        return self.title
    


class Shortment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.content
    

class Rank(models.Model):
    movie = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
