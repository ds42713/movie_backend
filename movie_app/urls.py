from django.contrib import admin
from django.db import router
from django.urls import path , include
from . import views


urlpatterns = [
    path('movie/',views.MovieGenericsView.as_view()),
    path('category/',views.CategoryAPIView.as_view()),
    path('movie/<str:slug>/',views.MovieItemView.as_view()),
]
