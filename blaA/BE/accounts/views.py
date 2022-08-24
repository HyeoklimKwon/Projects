from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from rest_framework.generics import GenericAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from accounts.pagination import CustomPageNumberPagination, CustomPagehundredNumberPagination
from notifications.models import Notification
from accounts.models import User
from rest_framework.decorators import api_view,permission_classes
from accounts.serializers import  (RegisterSerializer,LoginSerializer, UserCrewSerializer, UserListSerializer, UserReviewSerializer,
                                   UserSerializer,ChangePasswordSerializer,
                                   NicknameUniqueCheckSerializer,EmailUniqueCheckSerializer,UserNoneImageSerializer)
from rest_framework import response,status,permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.
from django import http
import requests
from rest_framework.authentication import get_authorization_header
from django.conf import settings
import jwt
from datetime import datetime, timedelta

# JWT_PAYLOAD_HANDLER = settings.JWT_AUTH['JWT_PAYLOAD_HANDLER']
# JWT_ENCODE_HANDLER = settings.JWT_AUTH['JWT_ENCODE_HANDLER']
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from crews.models import Crew

#user 확인 API 
class AuthUserAPIView(GenericAPIView) :
    # authentication_classes=[]
    #인증된 유저만 (토큰 필요 )
    permission_classes=(permissions.IsAuthenticated,)
    #요청한 유저를 가져와서, serializer에 넣음 
    serializer_class = RegisterSerializer
    def get(self,request) :
        user = request.user
        serializers=RegisterSerializer(user)
        #유저의 정보를 가져옴 
        return Response({'user':serializers.data})
class UserListAPIView(ListAPIView) :
    # authentication_classes=[]
    #인증된 유저만 (토큰 필요 )
    permission_classes=(permissions.IsAuthenticated,)
    #요청한 유저를 가져와서, serializer에 넣음 
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

#회원가입 API (POST)
class RegisterAPIView(GenericAPIView) :
    #인증 불필요 
    authentication_classes=[]
    #회원가입 직렬화
    serializer_class=RegisterSerializer 

    #post 요청이 오면 
    def post(self,request) :
        #요청이 온 데이터로 serializer 
        serializers = self.serializer_class(data=request.data)  
        #오류가 발생하지 않으면 회원가입 승인 
        if serializers.is_valid(raise_exception=True) :
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

#로그인 API 
class LoginAPIView(GenericAPIView) :
    authentication_classes=[]
    serializer_class = LoginSerializer
    
    def post(self,request) :
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        
        user = authenticate(username=email,password=password)
        
        if user :
            serializer =  self.serializer_class(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message':"Invaild credentials,try again"},status=status.HTTP_401_UNAUTHORIZED)

class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    lookup_field ='user_pk'
    
    def put(self, request,user_pk, *args, **kwargs):
        if user_pk != request.user.user_pk :
            return Response({'message':"You do not have permission to change the user's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        return self.update(request, *args, **kwargs)

    
#유저 프로필 RUD API
class UserRetrieveUpdateDeleteAPIView(GenericAPIView):
    # authentication_classes=[]
    serializer_class = UserSerializer


    #요청한 user_pk로 유저 조회 
    def get_object(self, user_pk):
        try:
            return User.objects.get(user_pk=user_pk)
        #없는 유저이면 404에러 
        except User.DoesNotExist:
            raise http.Http404
    ## 'email','name','nickname','region','category','is_alba','image'
    #user 정보 조회 
    # @swagger_auto_schema(tags=["TO-DO 생성"], request_body=UserSerializer, query_serializer=UserSerializer)
    def get(self, request,user_pk, format=None):
        #user_pk로 user 가져오기 
        user = self.get_object(user_pk)
        #유저 정보 전달 
        serializer = UserSerializer(user)
        return Response(serializer.data)
    #회원정보 수정
    #수정 가능 사항
    ## 'name','nickname','region','category','is_alba','image'
    def put(self, request,user_pk, format=None):
        user = self.get_object(user_pk)
        #수정을 요청한 유저가 계정주인이 아니면
        #수정 불가 
        if request.user != user :
            return Response({'message':"You do not have permission to change the user's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        #아니면 회원정보 수정 

        if request.FILES.get('image') :
            serializer = UserSerializer(instance=user,data=request.data)
        else : 
            serializer = UserNoneImageSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #회원탈퇴
    def delete(self, request,user_pk, format=None):
        user = self.get_object(user_pk)
        #탈퇴를 요청한 유저가 계정주인이 아니면
        if request.user != user :
            return Response({'message':"You do not have permission to change the user's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        #아니면 회원탈퇴
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(User, user_pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                context = {
                    'result' : f'{request.user.nickname}님이 {person.nickname}을 Follow 취소'
                }
            else:
                person.followers.add(user)
                Notification.objects.create(type='follow',user=person,content=f'{request.user.nickname}님이 {person.nickname}을 Follow 했습니다.',redirect_pk=request.user.pk)
                context = {
                    'result' : f'{request.user.nickname}님이 {person.nickname}을 Follow'
                }
        return JsonResponse(context)
    return redirect('accounts:login')






class EmailUniqueCheck(CreateAPIView):
    authentication_classes=[]
    serializer_class = EmailUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            return Response(data={'detail':['You can use this email']}, status=status.HTTP_200_OK)
        else:
            # detail = dict()
            # detail['detail'] = serializer.errors['email']
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class NicknameUniqueCheck(CreateAPIView):
    authentication_classes=[]
    serializer_class = NicknameUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(data={'detail':['You can use this nickname']}, status=status.HTTP_200_OK)
        else:
            detail = dict()
            detail['detail'] = serializer.errors['nickname']
            return Response(data=detail, status=status.HTTP_400_BAD_REQUEST)



class UserCrewAPIView(ListAPIView) :
    serializer_class = UserCrewSerializer 
    lookup_field = 'user_pk'

    def list(self, request,user_pk, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(user_pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self,user_pk):
        # print(self.request.user)
        return User.objects.filter(user_pk=user_pk)

class UserReviewAPIView(ListAPIView) :
    serializer_class = UserReviewSerializer
    pagination_class = CustomPageNumberPagination 
    lookup_field = 'user_pk'

    def list(self, request,user_pk, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(user_pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def get_queryset(self,user_pk):
        # print(self.request.user)
        return User.objects.filter(user_pk=user_pk)


class FollowAPIView(ListAPIView) :

    serializer_class = UserListSerializer
    lookup_field = 'user_pk'
    queryset = User.objects.all()
    pagination_class = CustomPagehundredNumberPagination
    
    def list(self, request, *args, **kwargs):
        user = self.get_object()
        queryset = User.objects.all()
        type = request.GET.get('type', None)
        print(type)
        #내가 팔로우 하는 유저
        if type == 'following' :
            queryset = User.objects.filter(followers=user)
        
        #나를 팔로잉 하는 유저 
        elif type == 'follower' :
            queryset = User.objects.filter(followings=user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class KakaoSignInView(View):
    def get(self, request):
        client_id = "0f5982ee3aa76733f951e5add93878c1"
        redirect_uri = "http://127.0.0.1:8000/account/sign-in/kakao/callback"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )

class KakaoLogin(GenericAPIView) :
    authentication_classes=[]
    serializer_class = LoginSerializer
    
    def post(self,request) :

        data = request.data
        if User.objects.filter(email=data['email']) :
            user = User.objects.get(email=data['email']) 

            dt = datetime.now( ) + timedelta(days=60)
            token = jwt.encode({
                'id': user.pk,
                'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
            # print(json.load(token))

            context = {
                'email' : data['email'],
                'token' :str(token, 'utf-8')
            }
            
            return JsonResponse(context)
    # authentication_classes=[]
# # API_HOST = f'https://kapi.kakao.com/v2/user/me'
    
# # response = requests.get(API_HOST)
# # print(response)
# # text = json.loads(response.text)
# # print(response.status_code)
# # print(text)

# # print(json.loads(request.body))
# # data=json.loads(request.body)
# auth_header = get_authorization_header(request)
# # print(auth_header)
# #받은 header를 utf-8로 디코딩한다. 
# auth_data = auth_header.decode('utf-8')
# # print(auth_data)
# #token 형식이 Bearer + Token 이므로, ' '로 나눈다. 
# auth_token = auth_data.split(' ')
# print(auth_token)
# URL = f'https://kapi.kakao.com/v2/user/me'
# # token = '7LFdr9efDtY-y2oghj4VtF3FR-ZPIKyYwFQmNjRGCilwUQAAAYJnqUQx'
# headers = {'Authorization': f'Bearer {auth_token[1]}','Content-Type': 'application/json; charset=utf-8'}
# response = requests.get(URL, headers=headers)
# print(response)
# text = json.loads(response.text)
# print(response.status_code)
# print(text)
# print(text.get('properties').get('nickname'))

# serializer_class = RegisterSerializer
    
# data = {
#     "email" : text.get('kakao_account').get('email'),
#     "name" : text.get('properties').get('nickname'),
#     "password" : "asdwghoiwehvewo",
#     "nickname" : "dfdfef",
#     "region" : "defs",
#     "category" : "fwberbe",
#     "is_alba" : True,
        
#         }
        # return HttpResponse(data={'token':token},status=status.HTTP_200_OK)
    # else :
    #     #요청이 온 데이터로 serializer 
    #     serializers = serializer_class(data=data)  
    #     #오류가 발생하지 않으면 회원가입 승인 
    #     if serializers.is_valid(raise_exception=True) :
    #         serializers.save()
    #         token = serializers.data['token']
    #         print(token)
    #         print(type(token))
    #         token = token.split('\'')
    #         print(token)
    #         print(token[1])
    #         serializers.data['token'] = token[1]
    #         print(serializers.data)
    #         print(serializers.data['token'])
            
    #         return JsonResponse(serializers.data,status=status.HTTP_201_CREATED)
    #     return JsonResponse(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

        
class KakaoSignInCallbackView(View):
    def get(self, request):

        try:
            code = request.GET.get("code")                                       
            client_id = "0f5982ee3aa76733f951e5add93878c1"
            redirect_uri = "http://127.0.0.1:8000/account/sign-in/kakao/callback"
            
            
            token_request = requests.post(                                        
                f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
            )

            token_json = token_request.json()                                    

            error = token_json.get("error",None)

            if error is not None :
                return JsonResponse({"message": "INVALID_CODE"}, status = 400)

            access_token = token_json.get("access_token")
            
                                    

        except KeyError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)

        except access_token.DoesNotExist:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)
    
        
