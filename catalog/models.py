from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email


class Genre(models.Model):
    genre_id=models.AutoField(primary_key=True,null=False)
    genre_type = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return (self.genre_type)


class Movies(models.Model):
    movie_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30, null=False, blank=False,unique=True)
    imdb_score=models.FloatField()
    director=models.CharField(max_length=20)
    _99popularity=models.FloatField(max_length=4)
    genre=models.ManyToManyField(Genre,related_name="genres")


    def __str__(self):
        return  (self.name)

