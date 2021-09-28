from movie_app import serializers
from movie_app.models import Movie
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello')

######### API  #######
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
#######################

@api_view(['GET'])
def api_get_movie(request):
    movie = Movie.objects.all()
    if request.method == 'GET':
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_get_movie_id(request,pid):
    movie = Movie.objects.filter(id=pid)
    if request.method == 'GET':
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data)