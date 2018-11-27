Part 3: Team Write Up
Create a new file docs/submission_02.md file in your github repository. In this document your team must include the following document:

Relational Model:


Overview: A brief overview of your application. Please highlight any changes from your project proposal since the Project 1 submission.
Our team is creating an application where an individual can schedule a time, request a party of up to 5 people, and match with those people to watch a movie of their choice. It is called “Flick”. The whole idea of this application is so that no one has to watch a movie alone if they don’t want to, and can use this application to make friends around the UMass or Five College campuses. This application consists of 5 web pages, a homepage where all the movies are listed, a page where an individual can request to watch a specific movie at a certain time of their choice, and a location of their preference with people they want to watch it with.

Team Members: A list of your team members
Apoorva Karpurapu
Kuhu Wadhwa
Damin Zhang
Long To
Frick Shao
Kurtis Chau

Video Link: https://www.youtube.com/watch?v=fG1PbDdWRqk&feature=youtu.be
https://youtu.be/fG1PbDdWRqk

Design Overview: A design overview of your data model as implemented in Django, the important URL routes, and the implemented UI views. Please provide enough detail to demonstrate your team’s understanding of the material. 
As a design overview of our data model, as it is implemented in Django: the important UI views through this is index, user profile, movie request page, and movie matchbox page. The data model mock data includes The important URL path included are: 

 [




   path("index/", views.index, name="index"), #movie list page


   path("movie/<str:movie>/", views.movie, name="movie"),


   path("user/<str:user>", views.user, name="user"),


   path("matchbox/", views.matchbox, name="matchbox"),


]



Problems:
One of the problems we encountered during the project had to be that we were collaborating last minute, and ended up scrambling to finish.
Some of the django tasks, as in setup issues and so on.

Successes:
The successes we encountered through this project would be the combined team collaboration. It consisted of everyone working together in an efficient way.
Team members helped one another through the process.

	
		

	



