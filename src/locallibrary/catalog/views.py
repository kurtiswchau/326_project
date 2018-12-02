from django.shortcuts import render
#the urls here will change based on the names we give the templates and where we put the templates
from catalog.models import Movie, Profile, Request, Match, Genre
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
##picture of movie; urls for movie and username and index; using function instead of class
##what does match need; what primary key of movie; hard for users to remember id

from django.contrib.auth.decorators import login_required
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
# from catalog.models import Profile
from django.shortcuts import render, redirect
from catalog.forms import SignUpForm, EditProfileForm, GenreFilterForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def index(request):
    if request.method == 'POST':
        if(len(request.POST.getlist('genres'))==0):
            movie_list = Movie.objects.all().order_by('-date')[:25]
        else:
            selected_list = request.POST.getlist('genres')
            display_text = "".join(selected_list)
            selected_genre = []
            for g in Genre.objects.all():
                if(g.name in selected_list):
                    selected_genre.append(g)
            movie_list=Movie.objects.all().filter(genre__in=selected_genre).order_by('-date')[:25]
    else:
        movie_list = Movie.objects.all().order_by('-date')[:25]
    genre_list = Genre.objects.all()
    genreFilterForm = GenreFilterForm()
    genreFilterForm.fields['genres'].choices=[(g,g) for g in Genre.objects.all()]
    # movie_list = Movie.objects.all().order_by('-date')[:25]
    
    context = {
        "movie_list": movie_list,
        "genre_list":genre_list,
        "genreFilterForm":genreFilterForm,
        
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
        "day_of_week" : movie_object.date.weekday(),
		"duration" : movie_object.duration,
		"summary" : movie_object.summary,
		"request_list" : request_objects,
		"match_list" : match_objects,
		"movie_id": movie_object.movie_id,
		"picture_url": movie_object.picture_url,
        "genre" : movie_object.get_genres(),
	}
	return render(request, "movie.html", context=context)

def profile(request, profileUsername):
    if request.method == 'POST':
        user = request.user
        form = EditProfileForm(request.POST or None)
        if form.is_valid():
            user.profile.bio = form.cleaned_data['bio']
            user.profile.gender = form.cleaned_data['gender']
            user.profile.picture_url = form.cleaned_data['picture_url']
            user.save()
    user_objects = Profile.objects.filter(profileUsername=profileUsername)
    user_object = user_objects.first()
    if request.user.username==user_object.profileUsername:
        context = {
            "profileUsername" : user_object.profileUsername,
            "bio" : user_object.bio,
            "pic" : user_object.picture_url,
            "gender" : user_object.gender,
            "form" : EditProfileForm,
        }
    else:   
        context = {
            "profileUsername" : user_object.profileUsername,
            "bio" : user_object.bio,
            "pic" : user_object.picture_url,
            "gender" : user_object.gender,
        }
    return render(request, "user.html", context = context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


		
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.picture_url = form.cleaned_data.get('picture_url')
            user.profile.profileUsername = user.username
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            django_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginRedirect(request):
    return HttpResponseRedirect(
               reverse(profile, 
                       args=[request.user.username]))