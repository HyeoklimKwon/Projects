from rest_framework import serializers
from accounts.models import User

from crews.models import Crew, CrewInvite,CrewChat


class CrewCreateSerializer(serializers.ModelSerializer) :

    class Meta: 
        model = Crew
        fields= ('crew_pk','crew_leader','is_business','crew_name','crew_img','crew_explain','crew_region')
        read_only_fields = ('crew_leader',)

class CrewNoneImageCreateSerializer(serializers.ModelSerializer) :

    class Meta: 
        model = Crew
        fields= ('crew_pk','crew_leader','is_business','crew_name','crew_img','crew_explain','crew_region')
        read_only_fields = ('crew_leader','crew_img')


class CrewListSerializer(serializers.ModelSerializer) :
    crew_member_count = serializers.IntegerField(source='crew_member.count', read_only=True)
    crew_leader = serializers.CharField(source='crew_leader.nickname')
    class Meta: 
        model = Crew
        fields= ('crew_pk','crew_leader','is_business','crew_name','crew_img','crew_member_count')



class CrewNonImageSerializer(serializers.ModelSerializer) :
    crew_member_count = serializers.IntegerField(source='crew_member.count', read_only=True)
    crew_leader = serializers.CharField(source='crew_leader.nickname',read_only=True)
    # crew_img = serializers.ImageField(required=False)
    class Meta: 
        model = Crew
        fields= ('crew_pk','crew_name','crew_leader','crew_explain','crew_region','crew_img','crew_member_count','created_at')
        read_only_fields = ('crew_pk','crew_leader','crew_img')

class CrewSerializer(serializers.ModelSerializer) :
    crew_member_count = serializers.IntegerField(source='crew_member.count', read_only=True)
    crew_leader_pk = serializers.IntegerField(source='crew_leader.user_pk',read_only=True)
    crew_leader = serializers.CharField(source='crew_leader.nickname',read_only=True)
    # crew_img = serializers.ImageField(required=False)
    class Meta: 
        model = Crew
        fields= ('crew_pk','crew_name','crew_leader','crew_leader_pk','crew_explain','crew_region','crew_img','crew_member_count','created_at')
        read_only_fields = ('crew_pk','crew_leader',)

    def update(self, instance, validated_data):
        instance.crew_name = validated_data.get('crew_name', instance.crew_name)
        instance.crew_explain = validated_data.get('crew_explain', instance.crew_explain)
        instance.crew_region = validated_data.get('crew_region', instance.crew_region)

        try:
            images_data = self.context['request'].FILES.get('crew_img')
        except:
            images_data = None
        # print(validated_data.get())
        if images_data is not None:
            instance.crew_img = images_data

        instance.save()

        return instance

class CrewInviteListSerializer(serializers.ModelSerializer) :
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    category = serializers.CharField(source='user.category', read_only=True)
    image = serializers.ImageField(source='user.image', read_only=True)
    class Meta: 
        model = CrewInvite
        fields= '__all__'
        read_only_fields = ('crew','user')

class UserInviteListSerializer(serializers.ModelSerializer) :
    crew_name = serializers.CharField(source='crew.crew_name', read_only=True)
    crew_member_count = serializers.IntegerField(source='crew.crew_member.count', read_only=True)
    image = serializers.ImageField(source='crew.crew_img', read_only=True)
    class Meta: 
        model = CrewInvite
        fields= '__all__'
        read_only_fields = ('crew','user')

class CrewUserListSerializer(serializers.ModelSerializer) :
    # crew_member_count = serializers.IntegerField(source='crew.crew_member.count', read_only=True)
    # nickname = serializers.CharField(source='crew.crew_member.nickname', read_only=True)
    # image = serializers.ImageField(source='crew.crew_member.image', read_only=True)
    class Meta: 
        model = User
        fields= ('user_pk','nickname','image')
        # read_only_fields = ('crew','user')


class CrewChatSerializer(serializers.ModelSerializer) :
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    image = serializers.ImageField(source='user.image', read_only=True)
    class Meta: 
        model = CrewChat 
        fields = ('chat_pk','user','crew','nickname','image','content','created_at')
        read_only_fields = ('crew','user')


class GetRequestSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=10)