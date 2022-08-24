from rest_framework import serializers
from .models import Blacklist
from accounts.models import User

class BlacklistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blacklist
        fields = '__all__'