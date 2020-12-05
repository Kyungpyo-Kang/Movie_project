from django.shortcuts import render
from .models import Movie



def home(request):
    return render(request, 'index.html')

def family_show(request):
    return render(request, 'family.html')

def family_pro(request):
    movies = Movie.objects.filter(genreAlt__contains='가족')
    movie_list = []
    for movie in movies:
        movie_list.append(movie)
    return render(request, 'family.html', {'movies':movie_list})

def couple_show(request):
    movies = Movie.objects.filter(genreAlt__contains='멜로/로맨스')
    movie_list = []
    for movie in movies:
        movie_list.append(movie)
    return render(request, 'couple.html', {'movies':movie_list})

def solo_show(request):
    movies = Movie.objects.filter(genreAlt__contains='액션')
    movie_list = []
    for movie in movies:
        movie_list.append(movie)
    return render(request, 'solo.html', {'movies':movie_list})

def result_show(request):
    movies = Movie.objects.filter(movieNm__contains=request.GET['movieNm'])
    movie_list = []
    for movie in movies:
        movie_list.append(movie)
    return render(request, 'result.html', {'movies':movie_list})