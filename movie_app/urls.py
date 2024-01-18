from django.urls import path
from . import views
from .views import DirectorListView, DirectorDetailView, MovieListView, MovieDetailView, ReviewListView, ReviewDetailView, MovieReviewsView, DirectorUpdateView, DirectorDeleteView, DirectorCreateView





urlpatterns = [
    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('movies/reviews/', MovieReviewsView.as_view(), name='movie-reviews'),
    path('api/v1/directors/', DirectorCreateView.as_view(), name='director_create'),
    path('api/v1/directors/<int:id>/', DirectorUpdateView.as_view(), name='director_update'),
    path('api/v1/directors/<int:id>/', DirectorDeleteView.as_view(), name='director_delete'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/confirm/<str:code>/', views.confirm_user, name='confirm-user'),
]

