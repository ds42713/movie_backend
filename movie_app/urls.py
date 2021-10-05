from django.contrib import admin
from django.db import router
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('movie-viewsets', views.MovieViewsets)
urlpatterns = [
    path('hello/', views.hello),
    #path('api/movie/get',views.api_get_movie),
    #path('api/movie/get/<int:pid>',views.api_get_movie_id),
    path('', include(router.urls)),
]
