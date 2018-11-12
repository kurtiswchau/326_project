
from django.db import models
from django_mysql.models import ListTextField
from django.urls import reverse

class Movie(models.Model):
    """Model representing a movie (but not a specific copy of a movie)."""

    title = models.CharField(max_length=200)
    cast = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the movie"
    )
    duration = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    genre = ListTextField(
        base_field=models.CharField(max_length=10),
        size=100,  # Maximum of 100 ids in list
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Request(models.Model):
    """Model representing a request."""
    username = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    # A character field for the first name.
    first_name = models.CharField(max_length=100)

    # A character field for the last name.
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    # A date field for when the request happen.
    date = models.DateField(null=True, blank=True)
    number_people = models.IntegerField(max_length=3)
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.last_name}, {self.first_name}"

class User(models.Model):
    username = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    password = models.CharField(max_lenght=300)
    id = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    pic = models.ImageField(upload_to='picpath/', default = 'pic_folder/None/no-img.jpg', blank=True, null=True)

    def __str__(self):
        return self.username
    

class Match(models.Model):
    username = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    request = models.ForeignKey("Request", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.username}, {self.request}"
    

