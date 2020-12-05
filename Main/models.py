from django.db import models

class Movie(models.Model):

    movieCd = models.IntegerField(primary_key=True)
    movieNm = models.CharField(max_length=20)
    openDt = models.CharField(max_length=10)
    typeNm = models.CharField(max_length=3)
    nationAlt = models.CharField(max_length=5)
    genreAlt = models.CharField(max_length=40)
    directors = models.CharField(max_length=20)
    showTm = models.CharField(max_length=5)
    userRating = models.CharField(max_length=8)

    def __str__(self):
        return self.movieNm
