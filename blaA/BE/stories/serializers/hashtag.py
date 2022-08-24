from rest_framework import serializers
from ..models import Hashtag
from ..models import Hashtag,Story
from accounts.models import User

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'
        read_only_fields = ('user_pk','story_pk')

class HashtagFilterSerializer(serializers.ModelSerializer):
    class StorySerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model =User
                fields = ('user_pk', 'nickname','image')
    
        user_pk = UserSerializer(read_only=True)
        class Meta:
            model =Story
            fields = ('user_pk','story_pk', 'story_title','story_picture')
    
    story_pk = StorySerializer(read_only=True)
    
    class Meta:
        model = Hashtag
        fields = ('story_pk','hashtag_content')
