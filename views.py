from django.shortcuts import render

# Create your views here.
from .models import Movie
from .models import User
from .models import Request
from .models import Match
##picture of movie; urls for movie and username and index; using function instead of class
##what does match need; what primary key of movie; hard for users to remember id
def index(request):
    movie_list = Movie.objects.all().order_by('-date')[:25]
    context = {
            "movie_list": movie_list}
    return render(
            request,
            "",##i think this should be index.html
            context
            )
##request.get_full_path()
    ##probably need something to get the image currently not in model
    ##order_by 25
def movie(request, title=None, director=None):
    ##what happens if two movies have same name
    movie_object = Movie.objects.filter(title=title, director=director)
    str = "movie/"## + movie_name
    context={
            "title": movie_object.title
            "cast": movie_object.cast
            "director": movie_object.director
            "summary": movie_object.summary
            "duration": movie_object.duration
            "date": movie_object.date
            }
    return render(
            request,
            str,
            context)
    
def user(request, userid=None):
    user_object = User.objects.filter(id=userid)
    str = "user/"## + str(user_id)
    context={
            "username" = user_object.username
            "bio" = user_object.bio
            "pic" = user_object.pic
            }
    return render(
            request,
            str,
            context)
    
def matchbox(request):
    ##i dont actually know what info is needed here
    context={
            }
    return render(
            request,
            "matchbox",
            context)
    
