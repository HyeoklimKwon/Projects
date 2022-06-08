from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Actor, Movie, Review
from .serializers import (
    ActorListSerializer, 
    ActorSerializer, 
    MovieListSerializer,
    MovieSerializer,
    ReviewListSerializer,
    ReviewSerializer,
    ReviewCreateSerializer,
    ReviewUpdateSerializer
)
# Create your views here.

# Actor 출력
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.order_by('-pk')
        serializer = ActorListSerializer(actors, many = True)
        return Response(serializer.data)

# Actor Movie에 등록
@api_view(['POST'])
def register_actor(request, actor_pk ,movie_pk):
    actor = get_object_or_404(Actor, pk = actor_pk)
    movie = get_object_or_404(Movie, pk = movie_pk)
    actor.movies.add(movie)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)        

# Actor Detail, 삭제, 갱신
@api_view(['GET', 'DELETE', 'PUT'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk = actor_pk)
    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        actor.delete()
        data = {
            'delete': f'데이터 {actor_pk}번 배우 정보가 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ActorSerializer(actor, request.data)        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
#======================================================================

# Movie GET: 요약 , POST: 생성
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-pk')
        serializer = MovieListSerializer(movies, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# Movie Detail, 삭제, 갱신
@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        data = {
            'delete': f'데이터 {movie_pk}번 영화 정보가 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, request.data)        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

#=======================================================================
# Review 출력
@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

# Review detail 출력, 삭제, 갱신
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        # movie_pk = serializer.data.get('movie')
        # movie = get_object_or_404(Movie, pk = movie_pk)
        # serializer.data.movie = movie.title                  
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'데이터 {review_pk}번 리뷰가 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewUpdateSerializer(review, request.data)
        # serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            review_pk = serializer.data['id']
            review = get_object_or_404(Review, pk=review_pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)

# Review 생성
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movie)
        review_pk = serializer.data['id']
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review)        
        return Response(serializer.data, status=status.HTTP_201_CREATED)



