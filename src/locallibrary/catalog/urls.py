from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"), # movie list page
    path("signup", views.signup, name="signup"), # signup page
    path("login", auth_views.LoginView.as_view(template_name='login.html'),name="login" ),
    path("movie/<int:movie_id>", views.movie,name="movie"),
    # path("movie/<int:pk>", views.MovieDetailView.as_view(), name="movie-detail"),

    path("user/<str:username>", views.user,name="user") # took out name
]
