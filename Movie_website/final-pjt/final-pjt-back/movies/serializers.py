from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genre, Movie, Review

User = get_user_model()

# 전체 영화
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','overview','poster_path', )


# 전체 장르
class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


# 영화 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie', 'grade')
        read_only_fields = ('movie', )


# 단일 영화
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    genres = GenreListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'