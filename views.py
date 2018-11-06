from django.shortcuts import render

# Create your views here.
from .models import Movie
from .models import User
from .models import Request
from .models import Match
##picture of movie; urls for movie and username and index; using function instead of class
##what does match need; what primary key of movie; hard for users to remember id
def index(request):
    movie_list = Movie.objects.all()##can probably use a filter function with date somehow
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
    movie_objects = Movie.objects.filter(title=title, director=director)
    movie_object = movie_objects.first()
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
    user_objects = User.objects.filter(id=userid)
    user_object = user_objects.first()
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
    
def matchbox(request, username, date, location):
    ##matchbox_object = Matchbox.objects.filter(title = title, director = director)
    matchbox_objects = Request.objects.filter(username = username, date=date, location=location)
    matchbox_object = matchbox_objects.first()
    str = "matchbox/"## + movie_name
    context={
            "title": matchbox_object.title
            "cast": matchbox_object.cast
            "director": matchbox_object.director
            "summary": matchbox_object.summary
            "duration": matchbox_object.duration
            "date": matchbox_object.date
            "username" = matchbox_object.username
            "bio" = matchbox_object.bio
            "pic" = matchbox_object.pic
            "matchStatus" = matchbox_object.matchStatus
            }
    return render(
            request,
            "matchbox",
            context)

def request(request):
    request_object = Request.objects.filter(title = title, director = director)
    str = "request/"## + movie_name
    context={
            "title": request_object.title
            "cast": request_object.cast
            "director": request_object.director
            "summary": request_object.summary
            "duration": request_object.duration
            "date": request_object.date
            "username" = request_object.username
            "bio" = request_object.bio
            "pic" = request_object.pic
            "requestStatus" = request_object.requestStatus
            }
    return render(
            request,
            "request",
            context)
    
