import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User as adminUser
from faker import Faker

from catalog.models import Genre, Movie, Request, Profile, Match

fake = Faker()

# Create Genres
genres = [
    Genre(name="Science Fiction"),
    Genre(name="Satire"),
    Genre(name="Drama"),
    Genre(name="Adventure"),
    Genre(name="Romance"),
    Genre(name="Mystery"),
    Genre(name="Action"),
]

# Save the genres to the database
for genre in genres:
    genre.save()


# Create Movies
movies = []
for i in range(0, 15):
    m_id = fake.random_int(100000,200000)
    m_title = fake.job()
    m_cast = fake.name()
    m_director = fake.name()
    m_summary = fake.sentence()
    m_duration = fake.random_int(120, 200)
    m_date = fake.past_date(start_date="-30d", tzinfo=None)
    m_picture_url = "https://res.cloudinary.com/dbgclcola/image/upload/v1541981429/deadpool.jpg"
    #m_genre = Genre("Science Fiction")
    movie = Movie(
        title=m_title, cast=m_cast, director=m_director, summary=m_summary, 
        duration=m_duration, date=m_date, movie_id=m_id, 
        picture_url = m_picture_url
    )
    movie.save()
    movie.genre.add(genres[fake.random_int(0, len(genres)) - 1])
    movie.save()
    movies.append(movie)


# Create Users

# users = []
# for i in range(0, 10):
#     u_fname = fake.first_name()
#     u_lname = fake.last_name()
#     u_username = u_fname + u_lname
#     u_password = fake.itin()
#     u_bio = fake.text(50)
#     u_picture_url = "https://res.cloudinary.com/dbgclcola/image/upload/v1541982429/profilepic.jpg"
#     user = User(
#         username=u_username, password=u_password, bio=u_bio
#         )
#     user.save()
#     users.append(user)

print("Genre:")
for g in Genre.objects.all():
    print(g)


#    print(a)
#
# print("\nUser:")
# for b in User.objects.all():
#     print(b)
#
# Retrieve a random book from model and print it.

# Get all movie:

print('------------------')
print('All movies:')
for movie in Movie.objects.all():
    print("\nExample Movie:")
    print(f"Title: {movie.title}")
    print(f"Cast: {movie.cast}")
    print(f"Director: {movie.director}")
    print(f"Summary:\n{movie.summary}")

user1 = adminUser.objects.create_user("user1","user1@326.edu","user1password")
user1.save()
user1.profile.bio = "user1 bio"
user1.profile.gender = "user1 gender"
user1.profile.picture_url = "https://res.cloudinary.com/dbgclcola/image/upload/v1541982429/profilepic.jpg"
user1.profile.profileUsername = "user1"
user1.save()

user1 = adminUser.objects.create_user("user2","user2@326.edu","user2password")
user1.save()
user1.profile.bio = "user2 bio"
user1.profile.gender = "user2 gender"
user1.profile.picture_url = "https://res.cloudinary.com/dbgclcola/image/upload/v1541982429/profilepic.jpg"
user1.profile.profileUsername = "user2"
user1.save()


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = adminUser.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)
