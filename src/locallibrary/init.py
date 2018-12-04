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

movies=[]
new_mov = Movie(title="Creed II",
                cast="Michael B. Jordan, Sylvester Stallone, Tessa Thompson",
                director="Steven Caple Jr.",
                summary="Under the tutelage of Rocky Balboa, heavyweight contender Adonis Creed faces off against Viktor Drago, son of Ivan Drago.",
                duration=200,
                date="2018-11-22", ## format: YYYY-MM-DD
                movie_id= 100001,  ## 6 digit integer, no leading 0s
                picture_url="https://m.media-amazon.com/images/M/MV5BMTcxMjUwNjQ5N15BMl5BanBnXkFtZTgwNjk4MzI4NjM@._V1_.jpg",
                
                )
new_mov.save()
new_mov.genre.add(genres[6])
new_mov.save()

new_mov2 = Movie(title="Fantastic Beasts: The Crimes of Grindelwald",
                cast="Johnny Depp, Eddie Redmayne, Jude Law, Ezra Miller",
                director="David Yates",
                summary="In an effort to thwart Grindelwald's plans of raising pure-blood wizards to rule over all non-magical beings, Albus Dumbledore enlists his former student Newt Scamander, who agrees to help, unaware of the dangers that lie ahead. Lines are drawn as love and loyalty are tested, even among the truest friends and family, in an increasingly divided wizarding world.",
                duration=133,
                date="2018-11-16", ## format: YYYY-MM-DD
                movie_id= 100002,  ## 6 digit integer, no leading 0s
                picture_url="https://m.media-amazon.com/images/M/MV5BZjFiMGUzMTAtNDAwMC00ZjRhLTk0OTUtMmJiMzM5ZmVjODQxXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                )
new_mov2.save()
new_mov2.genre.add(genres[2])
new_mov2.save()
new_mov3 = Movie(title="Robin Hood", 
                cast="Taron Egerton, Jamie Foxx, Ben Mendelsohn",
                director="Otto Bathurst",
                summary= "Robin of Loxley (Taron Egerton) a war-hardened Crusader and his Moorish commander (Jamie Foxx) mount an audacious revolt against the corrupt English crown in a thrilling action-adventure packed with gritty battlefield exploits, mind-blowing fight choreography, and a timeless romance.",
                duration=116,
                date="2018-11-21", ## format: YYYY-MM-DD
                movie_id= 100003,  ## 6 digit integer, no leading 0s
                picture_url="https://m.media-amazon.com/images/M/MV5BOGQzZDM0NGUtZGE1NS00ZjQwLTk0N2EtMWI0NTgxYTkwYWQ4XkEyXkFqcGdeQXVyNDMzMzI5MjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                
                )
new_mov3.save()
new_mov3.genre.add(genres[3])
new_mov3.save()
new_mov4 = Movie(title="Widows", 
                cast=" Viola Davis, Michelle Rodriguez, Elizabeth Debicki",
                director=" Steve McQueen",
                summary= "Set in contemporary Chicago, amid a time of turmoil, four women with nothing in common except a debt left behind by their dead husbands' criminal activities, take fate into their own hands, and conspire to forge a future on their own terms.",
                duration=129,
                date="2018-11-16", ## format: YYYY-MM-DD
                movie_id= 100004,  ## 6 digit integer, no leading 0s
                picture_url="https://m.media-amazon.com/images/M/MV5BMjM3ODc5NDEyOF5BMl5BanBnXkFtZTgwMTI4MDcxNjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                
                )
new_mov4.save()
new_mov4.genre.add(genres[5])
new_mov4.save()
new_mov5 = Movie(title="Boy Erased", 
                cast="  Lucas Hedges, Nicole Kidman, Joel Edgerton",
                director=" Joel Edgerton",
                summary= "The son of a Baptist preacher is forced to participate in a church-supported gay conversion program after being forcibly outed to his parents.",
                duration=115,
                date="2018-11-16", ## format: YYYY-MM-DD
                movie_id= 100005,  ## 6 digit integer, no leading 0s
                picture_url="https://m.media-amazon.com/images/M/MV5BNzM2MzU1NTM4NF5BMl5BanBnXkFtZTgwNTMwMzI1NjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                
                )
new_mov5.save()
new_mov5.genre.add(genres[2])
new_mov5.save()
new_mov6 = Movie(title="The Front Runner", 
                cast="Hugh Jackman, Vera Farmiga, J.K. Simmons",
                director=" Jason Reitman",
                summary= "Gary Hart, former senator of Colorado, becomes the front-runner for the Democratic presidential nomination in 1987. Hart's intelligence, charisma and idealism makes him popular with young voters, leaving him with a seemingly clear path to the White House. All that comes crashing down when allegations of an extramarital affair surface in the media, forcing the candidate to address a scandal that threatens to derail his campaign and personal life.",
                duration=113,
                date="2018-11-21", ## format: YYYY-MM-DD
                movie_id= 100006,  ## 6 digit integer, no leading 0s
                picture_url="https://m.media-amazon.com/images/M/MV5BMTcyNTAxOTg4NV5BMl5BanBnXkFtZTgwMTMwNjQ2NjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                
                )
new_mov6.save()
new_mov6.genre.add(genres[2])
new_mov6.save()
new_mov7 = Movie(title="2.0", 
                cast="  Rajinikanth, Akshay Kumar, Amy Jackson",
                director="S. Shankar",
                summary= "Scientists help the government investigate a threat beyond understanding.",
                duration=150,
                date="2018-11-29", ## format: YYYY-MM-DD
                movie_id= 100007,  ## 6 digit integer, no leading 0s
                picture_url="https://m.media-amazon.com/images/M/MV5BOGNhMWE2YzktYzU0Yi00OGFlLTlhYzMtODBiOGFiZTM1YjI1XkEyXkFqcGdeQXVyODIwMDI1NjM@._V1_UY268_CR4,0,182,268_AL_.jpg",
                
                )
new_mov7.save()
new_mov7.genre.add(genres[5])
new_mov7.save()
new_mov8 = Movie(title="Overlord", 
                cast= "Jovan Adepo, Wyatt Russell, Mathilde Ollivier",
                director="Julius Avery",
                summary= "A small group of American soldiers find horror behind enemy lines on the eve of D-Day.",
                duration=110,
                date="2018-11-29", ## format: YYYY-MM-DD
                movie_id= 100008,  ## 6 digit integer, no leading 0s
                picture_url=" https://m.media-amazon.com/images/M/MV5BNzU0NTI1MTU2M15BMl5BanBnXkFtZTgwNTg4MDIzNjM@._V1_UX182_CR0,0,182,268_AL_.jpg ",
                
                )
new_mov8.save()
new_mov8.genre.add(genres[3])
new_mov8.save()

# movies = []
# for i in range(0, 15):
#     m_id = fake.random_int(100000,200000)
#     m_title = fake.job()
#     m_cast = fake.name()
#     m_director = fake.name()
#     m_summary = fake.sentence()
#     m_duration = fake.random_int(120, 200)
#     m_date = fake.past_date(start_date="-30d", tzinfo=None)
#     m_picture_url = "https://res.cloudinary.com/dbgclcola/image/upload/v1541981429/deadpool.jpg"
#     #m_genre = Genre("Science Fiction")
#     movie = Movie(
#         title=m_title, cast=m_cast, director=m_director, summary=m_summary, 
#         duration=m_duration, date=m_date, movie_id=m_id, 
#         picture_url = m_picture_url
#     )
#     movie.save()
#     movie.genre.add(genres[fake.random_int(0, len(genres)) - 1])
#     movie.save()
#     movies.append(movie)




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

user2 = adminUser.objects.create_user("user2","user2@326.edu","user2password")
user2.save()
user2.profile.bio = "user2 bio"
user2.profile.gender = "user2 gender"
user2.profile.picture_url = "https://res.cloudinary.com/dbgclcola/image/upload/v1541982429/profilepic.jpg"
user2.profile.profileUsername = "user2"
user2.save()


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

