from django.db.models import fields
from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerFiels()
    class Meta:
        model = Category
        fields = '__all__'

class Film_companySerializer(serializers.ModelSerializer):
    id = serializers.IntegerFiels()
    class Meta:
        model = Film_company
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerFiels()
    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerFiels()
    class Meta:
        model = Actor
        fields = '__all__'

class MovieImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerFiels()
    class Meta:
        model = MovieImage
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(many=True)
    actor = ActorSerializer(many=True)
    image_preview = MovieImageSerializer(many=True)
    director = DirectorSerializer(many=True)
    film_company = Film_companySerializer

    class Meta:
        model = Movie
        fields = '__all__'