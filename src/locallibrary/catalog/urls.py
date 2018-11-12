from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # movie list page
 
    path("movies/", views.movie, name="movies"),
    # path("movie/<int:pk>", views.MovieDetailView.as_view(), name="movie-detail"),

    path("users/", views.user, name="users")
]
