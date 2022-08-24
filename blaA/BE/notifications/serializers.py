from rest_framework import serializers

from notifications.models import Notification



class NotificationSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Notification
        fields = ('type','redirect_pk','user','content','view','created_at')

class NotificationEditSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Notification
        fields = ('type','redirect_pk','user','content','view','created_at')
        read_only_fields = ('type','redirect_pk','user','content','created_at')