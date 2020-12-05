import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Theatre.settings')
django.setup()

from Main.models import Movie

CSV_PATH = '/Users/kyungpyokang/Desktop/final_movie.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        Movie.objects.create(
                movieCd = row['movieCd'],
                movieNm = row['movieNm'],
                openDt = row['openDt'],
                typeNm = row['typeNm'],
                nationAlt = row['nationAlt'],
                genreAlt = row['genreAlt'],
                directors = row['directors'],
                showTm = row['showTm'],
                userRating = row['userRating'],
            )
