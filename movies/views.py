from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Movie
def home(request):
    return HttpResponse("Welcome to the Home Page")

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':data})

def details(request,id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/details.html', {'movie':data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title,year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')
def delete(request,id):
    try:
        movie = Movie.objects.get(pk=id)
        movie.delete()
    except:
        raise Http404("Movie not found")
    return HttpResponseRedirect('/movies')