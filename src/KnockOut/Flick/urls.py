from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'), #movie list page
    path('movie/<str:movie>/', views.movie, name='movie'),
    path('user/<str:user>', views.user, name='user'),
    path('matchbox/', views.matchbox, name='matchbox'),
]
