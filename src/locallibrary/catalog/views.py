from django.shortcuts import render
#the urls here will change based on the names we give the templates and where we put the templates
from catalog.models import Movie, User, Request, Match
from django.views import generic

##picture of movie; urls for movie and username and index; using function instead of class
##what does match need; what primary key of movie; hard for users to remember id
def index(request):
	movie_list = Movie.objects.all().order_by('-date')[:25]
	context = {
		"movie_list": movie_list,
	}
	return render(request, "index.html", context=context)

def movie(request, movie_id):
	movie_objects = Movie.objects.filter(movie_id=movie_id)
	movie_object = movie_objects.first()
	request_objects = Request.objects.filter(movie=movie_object)
	match_objects = Match.objects.filter(movie=movie_object)
	context = {
		"title" : movie_object.title,
		"director" : movie_object.director,
		"cast" : movie_object.cast,
		"date" : movie_object.date,
		"duration" : movie_object.duration,
		"summary" : movie_object.summary,
		"request_list" : request_objects,
		"match_list" : match_objects,
		"movie_id": movie_object.movie_id,
	}
	return render(request, "movie.html", context=context)

def user(request, username):
	user_objects = User.objects.filter(username=username)
	user_object = user_objects.first()
	context = {
		"username" : user_object.username,
		"bio" : user_object.bio,
		"pic" : user_object.picture_url,
	}
	return render(request, "user.html", context=context)

		
