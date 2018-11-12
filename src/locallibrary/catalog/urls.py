from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # movie list page
 
    path("movie/<int:movie_id>", views.movie,name="movie"),
    # path("movie/<int:pk>", views.MovieDetailView.as_view(), name="movie-detail"),

    path("user/<str:username>", views.user,name="user") # took out name
]
