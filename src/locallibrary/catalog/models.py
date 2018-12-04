from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction)"
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Movie(models.Model):
    """Model representing a movie (but not a specific copy of a movie)."""
    movie_id = models.BigIntegerField(default=111111)
    title = models.CharField(max_length=200)
    cast = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the movie"
    )
    duration = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this movie")
    picture_url = models.CharField(max_length=300,default="https://test.jpg")
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    def get_genres(self):
        return "\n".join([g.name for g in self.genre.all()])

class Request(models.Model):
    """Model representing a request."""
    username = models.ForeignKey("Profile", on_delete=models.SET_NULL, null=True)
    # # A character field for the first name.
    # first_name = models.CharField(max_length=100)

    # # A character field for the last name.
    # last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    # A date field for when the request happen.
    date = models.DateField(null=True, blank=True)
    number_people = models.IntegerField()
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, null=True)
    time = models.TimeField(blank=True,null=True)
    note = models.CharField(max_length=100, blank=True,null=True)
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.username};{self.movie};{self.note}"

class Profile(models.Model):
    profileUsername = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    picture_url = models.CharField(max_length=300,default="https://test.jpg")
    
    def __str__(self):
        return self.profileUsername

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    

class Match(models.Model):
    usernames = models.CharField(max_length=200,null=True)
    request = models.ForeignKey("Request", on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.usernames}, {self.request}"
    

