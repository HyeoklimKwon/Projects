from unicodedata import category
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import deque
from notifications.models import Notification
from .models import Hashtag, Story,Comment
from accounts.models import User
from .serializers.story import StoryLikeSerializer, StorySerializer,StoryDetailSerializer
from .serializers.comment import CommentSerializer
from .serializers.hashtag import HashtagSerializer
from django.db.models import Q
# Create your views here.

@api_view(['GET', 'POST'])
def story_list_or_create(request):
    
    def story_list():
        story = Story.objects.all()
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)
    
    def create_story():
        story_picture = request.FILES.get('story_picture')
        story_title = request.data['story_title']
        print(story_picture)
        data = {
            'story_picture': story_picture,
            'story_title' : story_title
        }
        
        print(data)
        
        serializer = StorySerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_pk = request.user, region = request.user.region, category = request.user.category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    if request.method == 'GET':
        return story_list()
    elif request.method == 'POST':
        return create_story()
    
@api_view(['GET', 'PUT', 'DELETE'])   
def story_detail_or_update_or_delete(request, story_pk):
    story = get_object_or_404(Story, story_pk=story_pk)
    def story_detail():
        print(request.user.user_pk)
        serializer = StoryDetailSerializer(story)
        return Response(serializer.data)
    
    def story_update() :
        # print("~~~~~~~"+request.user.user_pk)
        if request.user.user_pk == story.user_pk_id:
            print(story)
            serializer = StorySerializer(instance=story, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_pk = request.user, region = request.user.region, category = request.user.category)
                return Response(serializer.data)
            
    def story_delete() : 
        if request.user.user_pk == story.user_pk_id:
            story.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    if request.method == 'GET':
        return story_detail()
    elif request.method == 'PUT':
        # print(request.user.user_pk)
        # print(story.user_pk_id)
        if request.user.user_pk == story.user_pk_id:
            return story_update()
    elif request.method == 'DELETE':
        if request.user.user_pk == story.user_pk_id:
            return story_delete()

@api_view(['GET', 'POST'])
def comment_list_or_create(request, story_pk):
    def comment_list():
        story = get_object_or_404(Story, story_pk = story_pk)
        print(story)
        comments = Comment.objects.filter(story_pk=story)
        serializer = CommentSerializer(comments, many= True)
        return Response(serializer.data)
    
    def comment_create():
        story = get_object_or_404(Story, story_pk = story_pk)
        serializer = CommentSerializer(data=request.data)
        story_user = story.user_pk
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_pk = request.user, story_pk = story)
            Notification.objects.create(type='story',user=story_user,content=f'{request.user.nickname}님이 {story_user.nickname}의 게시글에 댓글을 남겼습니다.',redirect_pk=story_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return comment_list()
    elif request.method == 'POST':
        return comment_create()
    
# @api_view(['GET'])         
# def comment_list(request, story_pk):
#     story = get_object_or_404(Story, story_pk = story_pk)
#     print(story)
#     comments = get_list_or_404(Comment,story_pk=story)
#     serializer = CommentSerializer(comments, many= True)
#     return Response(serializer.data)
        
# @api_view(['POST'])        
# def comment_create(request):
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])  
def comment_update_or_delete(request, comment_pk):
    comment = get_object_or_404(Comment, comment_pk=comment_pk)
    def comment_update() :
        if request.user.user_pk == comment.user_pk_id:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_pk = request.user)
                return Response(serializer.data)
            
    def comment_delete() :
        if request.user.user_pk == comment.user_pk_id:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        
    if request.method == 'PUT':
        if request.user.user_pk == comment.user_pk_id:
            return comment_update()
    elif request.method == 'DELETE':
        if request.user.user_pk == comment.user_pk_id:
            return comment_delete()   
        
        
@api_view(['GET', 'POST'])        
def hashtag_list_or_create(request, story_pk):
    
    def hashtag_list():
        story = get_object_or_404(Story, story_pk = story_pk)
        print(story)
        hashtags = get_list_or_404(Hashtag,story_pk=story)
        serializer = HashtagSerializer(hashtags, many= True)
        return Response(serializer.data)
    
    def hashtag_create():
        story = get_object_or_404(Story, story_pk = story_pk)
        print(request.data)
        tmp_query = request.data.copy()
        print(request.data.__getitem__('hashtag_content'))
        tmp = request.data.__getitem__('hashtag_content').split(' ')
        print(tmp)
        
        print(len(tmp))
        for hash in range(len(tmp)):
            print(tmp[hash])
            tmp_query.__setitem__('hashtag_content',tmp[hash])
            print(tmp_query)
            serializer = HashtagSerializer(data=tmp_query)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_pk = request.user, story_pk = story)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
        
        
    if request.method == 'GET':
        return hashtag_list()
    elif request.method == 'POST':
        return hashtag_create()
    
# @api_view(['POST'])        
# def hashtag_create(request, story_pk):
#     story = get_object_or_404(Story, story_pk = story_pk)
#     serializer = HashtagSerializer(data=request.data)
#     print(serializer)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user_pk = request.user, story_pk = story)
#         return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
@api_view(['PUT','DELETE'])  
def hashtag_update_or_delete(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, hashtag_pk=hashtag_pk)
    def hashtag_update() :
        if request.user.user_pk == hashtag.user_pk_id:
            serializer = HashtagSerializer(instance=hashtag, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_pk = request.user)
                return Response(serializer.data)
            
    def hashtag_delete() :
        if request.user.user_pk == hashtag.user_pk_id:
            hashtag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    if request.method == 'PUT':
        if request.user.user_pk == hashtag.user_pk_id:
            return hashtag_update()
    elif request.method == 'DELETE':
        if request.user.user_pk == hashtag.user_pk_id:
            return hashtag_delete()   
        
@api_view(['GET'])        
def follow_story_list(request):
    tmp = request.user.followings.all()
    if tmp :
        print(tmp)
        story = Story.objects.filter(user_pk=tmp[0])
        for user in range(1,len(tmp)) :
            story_res = story | Story.objects.filter(user_pk=tmp[user])
            story=story_res
            
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)
    
    else :
        story = Story.objects.filter(~Q(user_pk=request.user.user_pk))
        serializer = StorySerializer(story, many=True)
        response_data = serializer.data
        response_data.insert(0,{"message" : f"{request.user.nickname} doesn't follow any users yet."})
    return Response(response_data)
   
@api_view(['POST'])     
def like_story(request, story_pk):
    story = get_object_or_404(Story, story_pk=story_pk)
    user = request.user
    if story.like_user.filter(user_pk=user.pk).exists():
        story.like_user.remove(user)
        serializer = StoryLikeSerializer(story)
    else:
        story.like_user.add(user)
        serializer = StoryLikeSerializer(story)
    return Response(serializer.data)

@api_view(['GET'])   
def story_region_filter(request):
    story = Story.objects.filter(Q(region= request.user.region)&~Q(user_pk = request.user))
    # story = get_list_or_404(Story, region= request.user.region, user_pk != request.user)
    serializer = StorySerializer(story, many=True)
    return Response(serializer.data)

@api_view(['GET'])   
def story_category_filter(request):
    story = Story.objects.filter(Q(category= request.user.category)&~Q(user_pk = request.user))
    # story = get_list_or_404(Story, category= request.user.category)
    serializer = StorySerializer(story, many=True)
    return Response(serializer.data)

@api_view(['GET'])   
def story_both_filter(request):
    story = Story.objects.filter(Q(region= request.user.region)&Q(category= request.user.category)&~Q(user_pk = request.user))
    # story = get_list_or_404(Story, category= request.user.category)
    serializer = StorySerializer(story, many=True)
    return Response(serializer.data)

@api_view(['GET'])   
def mystory_list(request,user_pk):
    story = Story.objects.filter(Q(user_pk=user_pk))
    serializer = StorySerializer(story, many=True)
    return Response(serializer.data)
    