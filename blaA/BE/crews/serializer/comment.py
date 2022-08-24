from rest_framework import serializers
from accounts.models import User

from crews.models import Crew,CrewArticle,CrewArticleImage,CrewArticleComment


class UserSerializerComent(serializers.ModelSerializer) :
    class Meta: 
        model = User
        fields = ('user_pk','nickname','image')

class CrewCommentSerializer(serializers.ModelSerializer) :
    nickname = serializers.CharField(source='user.nickname',read_only=True)
    image = serializers.ImageField(source='user.image',read_only=True)
    # user_pk = serializers.IntegerField(source='user.user_pk')
    # crew_leader = serializers.CharField(source='crew_leader.nickname')
    # user = UserSerializerComent(read_only=True)
    class Meta: 
        model = CrewArticleComment
        fields= ('crew_comment_pk','crew','article','comment_content','user','nickname','image','created_at','updated_at')
        read_only_fields = ('crew','article','user')
