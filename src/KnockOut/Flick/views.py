from django.shortcuts import render
#the urls here will change based on the names we give the templates and where we put the templates
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
            "title": movie_object.title,
            "cast": movie_object.cast,
            "director": movie_object.director,
            "summary": movie_object.summary,
            "duration": movie_object.duration,
            "date": movie_object.date,
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
            "username" : user_object.username,
            "bio" : user_object.bio,
            }
    return render(
            request,
            str,
            context)
    
def matchbox(request, username, date, location):
    ##matchbox_object = Matchbox.objects.filter(title = title, director = director)
    matchbox_objects = Request.objects.filter(username = username, date=date, location=location)
    matchbox_object = matchbox_objects.first()
    ##needs to have related name in model
    movie = matchbox_object.movie_set.all().first()
    user = matchbox_object.user_set.all().first()
    str = "matchbox/"## + movie_name
    context={
            "title": movie.title,
            "cast": movie.cast,
            "director": movie.director,
            "summary": movie.summary,
            "duration": movie.duration,
            "date": movie.date,
            "username" : user.username,
            "bio" : user.bio,
            "pic" : user.pic,
            ##"matchStatus" = matchbox_object.matchStatus
            }
    return render(
            request,
            "matchbox",
            context)
##matchbox and request currently following relation backwards to get the user; maybe there is a better way?
def request(request):
    request_objects = Request.objects.filter(title = title, director = director)
    request_object = request_objects.first()
    str = "request/"## + movie_name
    movie = request_object.movie_set.all().first()
    user = request_object.user_set.all().first()
    context={
            "title": movie.title,
            "cast": movie.cast,
            "director": movie.director,
            "summary": movie.summary,
            "duration": movie.duration,
            "date": movie.date,
            "username" : user.username,
            "bio" : user.bio,
            "pic" : user.pic,
            "requestStatus" : request_object.requestStatus,
            }
    return render(
            request,
            "request",
            context)
