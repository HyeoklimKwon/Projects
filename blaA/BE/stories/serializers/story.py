from django.shortcuts import get_object_or_404
from rest_framework import serializers

from stories.serializers.comment import CommentSerializer
from stories.serializers.hashtag import HashtagSerializer
from ..models import Story,Comment,Hashtag
from accounts.models import User


class StorySerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model =User
            fields = ('user_pk', 'nickname','image')
    
    user_pk = UserSerializer(read_only=True)
    story_picture = serializers.ImageField()
    # count = serializers.SerializerMethodField()

    # def get_count(self,obj) :
    #     cnt = Story.objects.all().count()
    #     return cnt

    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ('user_pk','region','category','user_pk','like_user')




class StoryDetailSerializer(serializers.ModelSerializer) :
    
    class HashtagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Hashtag
            fields = ('hashtag_pk','hashtag_content')
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('user_pk','comment_pk','created_at','story_comment')
            
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model =User
            fields = ('user_pk', 'nickname','image')
    
    user_pk = UserSerializer(read_only=True)
            
    comment_set = CommentSerializer(read_only=True,many=True)
    hashtag_set = HashtagSerializer(read_only=True,many=True)

    # comment = get_object_or_404(Comment)
    like_user_count = serializers.IntegerField(source='like_user.count', read_only=True)
    class Meta :
        model = Story
        fields= ('story_pk','user_pk','story_title','story_picture','like_user','like_user_count','created_at','comment_set', 'hashtag_set')
        
class StoryLikeSerializer(serializers.ModelSerializer) :
    like_user_count = serializers.IntegerField(source='like_user.count', read_only=True)

    class Meta: 
        model = Story 
        fields = ('like_user','like_user_count')

