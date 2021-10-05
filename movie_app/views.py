from django.db.models import query
from movie_app import serializers
from movie_app.models import Movie
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

def hello(request):
    return HttpResponse('hello')

######### API  #######
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
#######################




class MovieViewsets(viewsets.ReadOnlyModelViewSet): 
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializers_class = MovieSerializer
    
