from rest_framework.generics import CreateAPIView
from rest_framework import generics
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from django.db.models import Avg, Count
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from .models import Director
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie
class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movies'))
    serializer_class = DirectorSerializer

class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class MovieReviewsView(generics.ListAPIView):
    queryset = Movie.objects.annotate(rating=Avg('reviews__stars'))
    serializer_class = MovieSerializer

class DirectorCreateView(LoginRequiredMixin, CreateAPIView):
    model = Director
    fields = ['name']

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return DirectorSerializer
        return DirectorSerializerReadOnly

class DirectorUpdateView(UpdateAPIView):
    model = Director
    fields = ['name']

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return DirectorSerializer
        return DirectorSerializerReadOnly


class DirectorDeleteView(DestroyAPIView):
    model = Director

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return DirectorSerializer
        return DirectorSerializerReadOnly

class MovieCreateView(LoginRequiredMixin, CreateAPIView):
    model = Movie
    fields = ['title', 'description', 'director', 'duration']

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return MovieSerializer
        return MovieSerializerReadOnly