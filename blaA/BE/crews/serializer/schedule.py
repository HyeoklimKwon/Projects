from rest_framework import serializers
from accounts.models import User

from crews.models import CrewSchedule

class CrewScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewSchedule
        fields = ('user', 'crew_day', 'color', 'crew_starthour','crew_endhour')
        read_only_fields = ('crew',)


class CrewScheduleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='user.image')
    nickname = serializers.CharField(source='user.nickname')
    class Meta:
        model = CrewSchedule
        fields = ('user','image', 'nickname', 'color', 'crew_starthour','crew_endhour')
        read_only_fields = ('crew','image','nickname')

class UserScheduleSerializer(serializers.ModelSerializer) :
    class Meta() :
        model=User
        fields= ('user_pk','nickname','image')
