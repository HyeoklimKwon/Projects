from rest_framework import serializers
from ..models import Comment
from accounts.models import User



class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model =User
            fields = ('user_pk', 'nickname','image')
            
    user_pk = UserSerializer(read_only=True)
    
    class Meta :
        model = Comment
        fields = ('comment_pk','user_pk','story_comment','created_at')

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('user_pk','story_pk')