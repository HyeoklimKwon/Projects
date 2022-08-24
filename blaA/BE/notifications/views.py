from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from notifications.serializers import NotificationEditSerializer
from notifications.models import Notification
from rest_framework.response import Response
from rest_framework import status
from notifications.serializers import NotificationSerializer
# Create your views here.


class NotificationListAPIView(ListAPIView) :

    serializer_class = NotificationSerializer
    
    
    queryset=Notification.objects.all()
    
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class NotificationDestoryAPIView(RetrieveUpdateDestroyAPIView) :
    lookup_field = 'pk'
    queryset=Notification.objects.all()
    serializer_class  = NotificationEditSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user :
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else : 
            return Response({'message':"You do not have permission to remove the notification,try again"},status=status.HTTP_400_BAD_REQUEST)


