from django.views.generic import ListView, DetailView

from walken.models import Movie, File

class MovieList(ListView):
    model = Movie

class FileList(ListView):
    model = File

class MovieDetail(DetailView):
    model = Movie
