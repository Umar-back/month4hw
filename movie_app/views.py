from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
        return DirectorSerializer

class DirectorUpdateView(UpdateAPIView):
    model = Director
    fields = ['name']

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return DirectorSerializer
        return DirectorSerializer

class DirectorDeleteView(DestroyAPIView):
    model = Director

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return DirectorSerializer
        return DirectorSerializer

class MovieCreateView(LoginRequiredMixin, CreateAPIView):
    model = Movie
    fields = ['title', 'description', 'director', 'duration']

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return MovieSerializer
        return MovieSerializer


@api_view(['GET', 'POST'])
def test_api_view(request):
    if request.method == 'GET':
        dict_ = {
            "text": 'hello',
            "int": 100,
            "float": 3.14,
            "bool": True,
            "list": [1, 2, 3],
            "dict": {"a": 1, "b": 2},
        }
        return Response(data=dict_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print(request.data)
        return Response()


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ConfirmationCode


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['123456']
        password2 = request.POST['123456']

        if password1 != password2:
            return HttpResponse('Пароли не совпадают')

        user = User.objects.create_user(email, password1)
        code = ConfirmationCode.objects.create(user=user)

        return render(request, 'registration/confirmed.html', {'code': code.code})

    return render(request, 'registration/register.html')


def confirm_user(request, code):
    try:
        code_obj = ConfirmationCode.objects.get(code=code)
    except ConfirmationCode.DoesNotExist:
        return HttpResponse('Код не найден', status=404)

    user = code_obj.user
    user.is_active = True
    user.save()

    return render(request, 'registration/confirmed.html')