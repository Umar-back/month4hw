from rest_framework import serializers, generics, validators
from .models import Director, Movie, Review
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.generics import CreateAPIView

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            'id',
            'name',
        ]
        extra_kwargs = {
            'name': {'min_length': 2, 'max_length': 255, 'required': True}
        }


class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'
    lookup_value_regex = '[0-9]'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['__all__']

        extra_kwargs = {
            'title': {'min_length': 1, 'max_length': 255},
            'description': {'min_length': 1, 'max_length': 1000}
        }

        validators = [
            MinValueValidator(0),
            MaxValueValidator(240)
        ]


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
    lookup_value_regex = '[0-9]'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['__all__']

        extra_kwargs = {
            'user': {'min_length': 1, 'max_length': 255},
            'text': {'min_length': 1, 'max_length': 1000}
        }

        validators = [
            MinValueValidator(1),
            MaxValueValidator(10)
        ]


class DirectorCreateView(CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieCreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer