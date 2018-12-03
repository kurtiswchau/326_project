from django.contrib import admin

from catalog.models import Genre, Movie, Profile, Request, Match

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title","get_genres","cast","director","summary","duration","date","picture_url","movie_id"]
    list_filter = ["genre"]

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("username","location","date","time","number_people","movie")

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("usernames","request")

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display=("profileUsername","gender","bio","picture_url")






