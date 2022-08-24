from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from accounts import serializers
from rest_framework import response,status,permissions
from rest_framework.response import Response
from accounts.models import User

from blacklists.serializers import BlacklistSerializer

class BlacklistAPIView(GenericAPIView) :
    
    serializer_class = BlacklistSerializer
    
    def post(self,request) :
        print(request.data)
        
        serializers = self.serializer_class(data=request.data)
        
        if serializers.is_valid(raise_exception=True) :
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        