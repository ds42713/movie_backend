from django.db.models import query
from movie_app import serializers
from movie_app.models import Movie
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

######### API  #######
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
#######################

class MovieGenericsView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieItemView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer  
    lookup_field = 'slug'

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
