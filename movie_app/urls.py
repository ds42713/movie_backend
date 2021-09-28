from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('api/movie/get',views.api_get_movie),
    path('api/movie/get/<int:pid>',views.api_get_movie_id)
]