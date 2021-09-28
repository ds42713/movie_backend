from django.db.models import fields
from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Film_companySerializer(serializers.ModelSerializer):
    class Meta:
        model = Film_company
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True,many=True)
    film_company = Film_companySerializer(read_only=True)
    director = DirectorSerializer(read_only=True,many=True)
    actor = ActorSerializer(read_only=True,many=True)
    movieImage = MovieImageSerializer(read_only=True,many=True)

    class Meta:
        model = Movie
        fields = '__all__'