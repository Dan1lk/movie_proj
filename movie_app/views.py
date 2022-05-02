from django.shortcuts import render, get_object_or_404
from . models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
# Create your views here.

def show_all_movie(request):
    #movies = Movie.objects.order_by(F('year').desc(nulls_first=True), '-rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_bool=Value('hello'),
        int_bool=Value(20),
        new_budget=F('budget')+100,
        sum_rat_year=F('rating') + F('year')
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('rating'))

    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg
    })

def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

def show_all_directors(request):
    directors = Director.objects.all
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors
    })

def show_one_director(request, id_dir: int):
    dir = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/one_director.html', {
        'dir': dir
    })

def show_all_actors(request):
    actors = Actor.objects.all
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors
    })

def show_one_actor(request, id_act: int):
    act = get_object_or_404(Actor, id=id_act)
    return render(request, 'movie_app/one_actor.html', {
        'act': act
    })