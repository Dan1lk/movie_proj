from django.shortcuts import render, get_object_or_404
from . models import Movie
from django.db.models import F
# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').desc(nulls_first=True), '-rating')
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })

def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })