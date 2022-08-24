from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from categorys.models import Dong, Gugun, JobCategory, Sido
from categorys.serializers import DongSerializer, JobSerializer, SidoSerializer,GugunSerializer
from django.db.models import Q

# Create your views here.
class SidoListAPIView(ListAPIView):
    #요청한 user_pk로 유저 조회 
    authentication_classes=[]
    queryset = Sido.objects.all()
    serializer_class = SidoSerializer
    ## 시/도 조회 
    def list(self, request):
        #user_pk로 user 가져오기 
        #유저 정보 전달 
        queryset = self.get_queryset()
        serializer = SidoSerializer(queryset,many=True)
        return Response(serializer.data)
    
class GugunListAPIView(ListAPIView):
    #요청한 user_pk로 유저 조회 
    authentication_classes=[]
    ## 시/도 조회 
    # lookup_field = 'sido'
    queryset = Gugun.objects.all()
    serializer_class = GugunSerializer
    def list(self, request,sido):
        #user_pk로 user 가져오기 
        #유저 정보 전달 
        # print(request.params)
        queryset = Gugun.objects.filter(Q(gugun_code__startswith=sido))
        serializer = GugunSerializer(queryset,many=True)
        return Response(serializer.data)

class DongListAPIView(ListAPIView):
    #요청한 user_pk로 유저 조회 
    authentication_classes=[]
    ## 시/도 조회 
    # lookup_field = 'sido'
    queryset = Dong.objects.all()
    serializer_class = DongSerializer
    def list(self, request,sido,gugun):
        #user_pk로 user 가져오기 
        #유저 정보 전달 
        tmp_sum = str(sido)+str(gugun)
        queryset = Dong.objects.filter(Q(dong_code__startswith=tmp_sum))
        serializer = DongSerializer(queryset,many=True)
        return Response(serializer.data)

class JobListAPIView(ListAPIView):
    #요청한 user_pk로 유저 조회 
    authentication_classes=[]
    ## 시/도 조회 
    # lookup_field = 'sido'
    serializer_class = JobSerializer
    queryset = JobCategory.objects.all()
    def list(self, request):
        queryset = self.get_queryset()
        serializer = JobSerializer(queryset,many=True)
        return Response(serializer.data)