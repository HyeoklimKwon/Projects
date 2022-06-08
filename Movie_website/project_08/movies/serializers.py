from rest_framework import serializers
from .models import Movie, Actor, Review

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many= True, read_only = True)

    class Meta:
        model = Actor
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
                
        fields = ('title', 'content', )
        read_only_fields = ('movie',  )

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer()

    class Meta:
        model = Review        
        fields = '__all__'

class ReviewUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class ReviewCreateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Review        
        exclude = ('movie', )
        


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorListSerializer(many = True, read_only = True)
    review_set = ReviewSerializer(many = True, read_only = True)

    class Meta:
        model = Movie
        fields = '__all__'