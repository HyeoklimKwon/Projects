from rest_framework import status
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView, DestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from notifications.models import Notification
from crews.serializer.crew import (CrewNonImageSerializer,CrewChatSerializer,CrewNoneImageCreateSerializer,
                                        CrewCreateSerializer, CrewInviteListSerializer, CrewListSerializer, CrewSerializer, 
                                        CrewUserListSerializer, UserInviteListSerializer,GetRequestSerializer)
from accounts.pagination import CustomPageNumberPagination, CustomPagehundredNumberPagination
from crews.serializer.schedule import CrewScheduleListSerializer,UserScheduleSerializer,CrewScheduleSerializer
from crews.models import Crew, CrewArticle, CrewArticleComment, CrewInvite, CrewSchedule,CrewChat
from rest_framework import filters
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from crews.serializer.article import CrewArticleRUDSerializer, CrewArticleSerializer
from crews.serializer.comment import CrewCommentSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from drf_yasg.utils import swagger_auto_schema
#리뷰를 작성할 가게 검색 or 가게 추가
class CrewListCreateAPIView(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = CrewCreateSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    queryset=Crew.objects.all()
    search_fields = ['crew_name']
    filterset_fields = ['is_business']
    pagination_class = CustomPagehundredNumberPagination 

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CrewListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CrewListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.FILES.get('crew_img') :
            serializer = self.get_serializer(data=request.data)
        else : 
            serializer = CrewNoneImageCreateSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(crew_leader=self.request.user)
        crew = Crew.objects.get(pk=serializer.data['crew_pk'])
        crew.crew_member.add(self.request.user)
        return serializer.data


#크루 상세조회, 크루 변경, 크루 삭제
# 변경 삭제는 크루 리더만 
class CrewRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView) :

    # authentication_classes=[]
    serializer_class = CrewSerializer
    queryset=Crew.objects.all()
    lookup_field = 'crew_pk'


    def update(self, request,crew_pk, *args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_pk)
        if request.user != crew.crew_leader :
            return Response({'message':"You do not have permission to change the user's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if request.FILES.get('crew_img') :
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
        else : 
            serializer = CrewNonImageSerializer(instance,data= request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request,crew_pk, *args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_pk)
        if request.user != crew.crew_leader :
            return Response({'message':"You do not have permission to change the crew's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CrewArticleListCreateAPIView(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = CrewArticleSerializer
    queryset=CrewArticle.objects.all()
    lookup_field = 'crew_id'
    pagination_class = CustomPagehundredNumberPagination 

    def list(self, request, crew_id,*args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_id)
        if request.user in crew.crew_member.all() :

            queryset = CrewArticle.objects.filter(crew=crew_id).order_by('-crew_pin')
        else :
            queryset = CrewArticle.objects.filter(crew=crew_id,crew_private=False).order_by('-crew_pin')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, crew_id,*args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_id)
        if request.user in crew.crew_member.all() :
            serializer = self.get_serializer(data=request.data)
            print(request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(crew_id,serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else :
            return Response({'message':"You do not have permission to create the article in crew ,try again"},status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, crew_id,serializer):
        crew = Crew.objects.get(crew_pk=crew_id)
        serializer.save(user=self.request.user,crew=crew)
        return serializer.data



class CrewArticleRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView) :

    # authentication_classes=[]
    serializer_class = CrewArticleRUDSerializer
    queryset=CrewArticle.objects.all()
    lookup_field = 'crew_article_pk'


    def retrieve(self, request, crew_article_pk,*args, **kwargs):
        instance = self.get_object()
        crew_article = CrewArticle.objects.get(crew_article_pk=crew_article_pk)
        crew = Crew.objects.get(crew_pk=crew_article.crew_id)
        if crew_article.crew_private and not (request.user in crew.crew_member.all() ):
            return Response({'message':"You do not have permission to view the article's ,try again"},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def update(self, request,crew_article_pk, *args, **kwargs):
        article = CrewArticle.objects.get(crew_article_pk=crew_article_pk)
        
        if request.user != article.user :
            return Response({'message':"You do not have permission to change the article's information,try again"},status=status.HTTP_400_BAD_REQUEST)
    
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer,crew_article_pk)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer,crew_article_pk):
        # crew = Crew.objects.get(crew_pk=crew_id)
        serializer.save(crew_article_pk=crew_article_pk)
        return serializer.data


    def destroy(self, request,crew_article_pk, *args, **kwargs):
        article = CrewArticle.objects.get(crew_article_pk=crew_article_pk)
        if request.user != article.user :
            return Response({'message':"You do not have permission to change the article's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)




class CrewCommentListCreateAPIView(ListCreateAPIView):
    # authentication_classes=[]
    serializer_class = CrewCommentSerializer
    queryset=CrewArticleComment.objects.all()
    lookup_field = 'crew_article_pk'
    pagination_class = CustomPagehundredNumberPagination 

    def list(self, request, crew_article_pk,*args, **kwargs):
        queryset = CrewArticleComment.objects.filter(article=crew_article_pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, crew_article_pk,*args, **kwargs):
        article = CrewArticle.objects.get(crew_article_pk=crew_article_pk)
        crew = Crew.objects.get(crew_pk=article.crew_id)
        if request.user in crew.crew_member.all() :
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(crew.crew_pk,crew_article_pk,serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else :
            return Response({'message':"You do not have permission to create the article in crew ,try again"},status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, crew_id,crew_article_pk,serializer):
        crew = Crew.objects.get(crew_pk=crew_id)
        article = CrewArticle.objects.get(crew_article_pk=crew_article_pk)
        serializer.save(user=self.request.user,crew=crew,article=article)
        return serializer.data


class CrewCommentUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    # authentication_classes=[]
    serializer_class = CrewCommentSerializer
    queryset=CrewArticleComment.objects.all()
    lookup_field = 'crew_comment_pk'
    def update(self, request,crew_comment_pk, *args, **kwargs):
        comment = CrewArticleComment.objects.get(crew_comment_pk=crew_comment_pk)
        
        if request.user != comment.user :
            return Response({'message':"You do not have permission to change the comment's information,try again"},status=status.HTTP_400_BAD_REQUEST)
    
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # print(crew_id)
        self.perform_update(serializer,comment.crew_id,comment.article_id)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def perform_update(self, serializer,crew_id,crew_article_pk ):
        #print(crew_id,crew_article_pk)
        crew = Crew.objects.get(crew_pk=crew_id)
        article = CrewArticle.objects.get(crew_article_pk=crew_article_pk)
        serializer.save(user=self.request.user,crew=crew,article=article)
        return serializer.data

    def destroy(self, request,crew_comment_pk, *args, **kwargs):
        comment = CrewArticleComment.objects.get(crew_comment_pk=crew_comment_pk)
        if request.user != comment.user :
            return Response({'message':"You do not have permission to change the comment's information,try again"},status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])  
def crew_schedule_list_or_create(request, crew_id):
    
    def schedule_list():
        schedule = CrewSchedule.objects.filter(Q(crew_id=crew_id))
        serializer = CrewScheduleListSerializer(schedule, many = True)
        return Response(serializer.data)
    # @swagger_auto_schema(method='POST', request_body=CrewScheduleListSerializer)  
    def schedule_create():
        serializer = CrewScheduleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(crew_id=crew_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    if request.method == 'GET':
        return schedule_list()
    elif request.method == 'POST':
        return schedule_create()
    
@api_view(['PUT', 'DELETE'])  
def crew_schedule_update_or_delete(request, crew_schedule_pk):
    
    schedule = CrewSchedule.objects.get(crew_schedule_pk=crew_schedule_pk)
    
    def schedule_update():
        serializer = CrewScheduleListSerializer(instance=schedule, data=request.data)
        if serializer.is_valid(raise_exception=True):
                serializer.save(crew_id=schedule.crew_id)
                return Response(serializer.data)
            
    def schedule_delete():
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PUT':
        return schedule_update()
    elif request.method == 'DELETE':
        return schedule_delete()



@api_view(['GET'])
def crew_schedule_work_list(request,crew_id, schedule):
    work = request.GET.get('work', None)

    crew = Crew.objects.get(crew_pk=crew_id)
    
    schedule = crew.crewschedule_set.filter(crew_day=schedule)

    if int(work) :
        serializer = CrewScheduleSerializer(schedule, many = True)
    else : 
        schedule_user = []
        for s in schedule :
            schedule_user.append(s.user.user_pk)
        un_scedule_user = User.objects.filter(Q(crews=crew_id)&~Q(user_pk__in = schedule_user))
        serializer = UserScheduleSerializer(un_scedule_user,many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)
    



class CrewUserAPIView(ListAPIView) :
    lookup_field = 'crew_pk' 
    queryset = Crew.objects.all()
    serializer_class = CrewUserListSerializer
    pagination_class = CustomPagehundredNumberPagination 

    def list(self, request, *args, **kwargs):
        crew = self.get_object()
        queryset = User.objects.filter(crews=crew)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

#크루장이 초대할 때 
# invite/<int:crew_pk>/<int:user_pk>/ 이 주소로 보내면 일단 크루장이 초대를 하는거야 
@api_view(['POST'])
def CrewInviteView(request,crew_pk,user_pk) :
#  크루장이 초대를 하는 로직인데 

    crew = Crew.objects.get(crew_pk=crew_pk) 
    user = User.objects.get(user_pk=user_pk)
    
    #print(crew,user)
    #초대하려는 사람이 이미 크루에 있으면 
    if crew.crew_member.filter(user_pk=user_pk).exists() :
        return Response({'message':"The user you want to invite has already joined the crew. Invalid request."},status=status.HTTP_409_CONFLICT)
    
    #이미 초대한 유저이면 
    if CrewInvite.objects.filter(user=user_pk,crew=crew_pk) :
        return Response({'message':'You are already invited.'},status=status.HTTP_400_BAD_REQUEST)
    
    #둘다 아니면 초대목록에 추가 
    CrewInvite.objects.create(crew=crew,user=user,crew_leader_accept=True,user_accept=False)
    Notification.objects.create(type='crew_invite',user=user,content=f'{crew.crew_name}크루에서 {user.nickname}을 초대했습니다.',redirect_pk=crew_pk)
    return Response({'message':" You have been successfully invited."},status=status.HTTP_201_CREATED)

#유저가 가입신청할 때 
@api_view(['POST'])
def CrewSignView(request,crew_pk) :

    crew = Crew.objects.get(crew_pk=crew_pk) 
    user = request.user
    
    #이미 크루에 가입되어있으면 
    if crew.crew_member.filter(user_pk=user.user_pk).exists() :
        return Response({'message':"You are already a member of the crew. Invalid request."},status=status.HTTP_409_CONFLICT)
    
    #이미 가입신청한 
    if CrewInvite.objects.filter(user=user.user_pk,crew=crew_pk) :
        return Response({'message':'We are waiting for your approval to join. Invalid request.'},status=status.HTTP_400_BAD_REQUEST)
    
    #둘다 아니면 초대목록에 추가 
    CrewInvite.objects.create(crew=crew,user=user,crew_leader_accept=False,user_accept=True)

    return Response({'message':" You have successfully applied for membership."},status=status.HTTP_201_CREATED)




#크루에 초대한 유저 리스트
#유저의 가입승인을 기다리고 있는 리스트
#크루 가입신청 승인 
from drf_yasg  import openapi 
@api_view(['GET'])
@swagger_auto_schema(tags=['데이터를 검색합니다.'],query_serializer=GetRequestSerializer,responses={200: 'Success'})  
def InviteSignListCrewView(request,crew_pk) :
    crew = Crew.objects.get(crew_pk=crew_pk)
    if request.user != crew.crew_leader :
        return Response({'message':"The request is not authorized."},status=status.HTTP_401_UNAUTHORIZED)   

    type = request.GET.get('type', None)
    query = CrewInvite.objects.filter(crew=crew)
    #크루에 초대한 유저 리스트
    if type == 'invite' :
        query = CrewInvite.objects.filter(crew=crew,user_accept=False)
    
    #크루에 가입신청한 유저 리스트
    elif type == 'sign' :
        query = CrewInvite.objects.filter(crew=crew,user_accept=True)

    serializer = CrewInviteListSerializer(query, many = True)
    return Response(serializer.data)



#크루장이 유저의 가입 요청 승인하기
@api_view(['POST'])
def AcceptUserView(request,crew_pk,user_pk) :
    crew = Crew.objects.get(crew_pk=crew_pk)
    user = User.objects.get(user_pk=user_pk)

    #크루리더가 아니면 리턴 
    if request.user != crew.crew_leader :
        return Response({'message':"The request is not authorized."},status=status.HTTP_401_UNAUTHORIZED)   

    #이미 크루에 있는 유저면 리턴 
    if crew.crew_member.filter(user_pk=user.user_pk).exists() :

        return JsonResponse({'message':"You are already a registered user."},status=status.HTTP_400_BAD_REQUEST)

    #둘다 아니면 크루에 추가 
    obj = CrewInvite.objects.get(crew=crew,user=user,user_accept=True) 
    if obj :
        crew.crew_member.add(user) 
        obj.delete() 
        Notification.objects.create(type='crew',user=user,content=f'{user.nickname}이 {crew.crew_name}크루에 가입되었습니다.',redirect_pk=crew_pk)
        data = {
            'message':f"{user.nickname}님이 {crew.crew_name}에 가입하셨습니다."
        }
        return JsonResponse(data)
    else : 
        data = {
            'message':"Error"
        }
        return JsonResponse(data)
#크루장이 유저의 가입 요청 거절하기
@api_view(['POST'])
def DenyUserView(request,crew_pk,user_pk) :
    crew = Crew.objects.get(crew_pk=crew_pk)
    user = User.objects.get(user_pk=user_pk)

    #크루리더가 아니면 리턴 
    if request.user != crew.crew_leader :
        return Response({'message':"The request is not authorized."},status=status.HTTP_401_UNAUTHORIZED)   

    #이미 크루에 있는 유저면 리턴 
    if crew.crew_member.filter(user_pk=user.user_pk).exists() :

        return JsonResponse({'message':"You are already a registered user."},status=status.HTTP_400_BAD_REQUEST)

    #둘다 아니면 가입 테이블 삭제
    obj = CrewInvite.objects.get(crew=crew,user=user,user_accept=True) 
    if obj :
        obj.delete() 
        data = {
            'message':f"{user.nickname}님의 {crew.crew_name} 크루 가입을 거절하셨습니다."
        }
        return JsonResponse(data)
    else : 
        data = {
            'message':"Error"
        }
        return JsonResponse(data)

#유저에게 가입신청 보낸 크루 리스트
#유저가 가입신청한 크루 리스트 
@api_view(['GET'])
@swagger_auto_schema(method='GET')
def InviteSignListUserView(request) :
    user = request.user
    query = CrewInvite.objects.filter(user=user)
    type = request.GET.get('type', None)
    #유저에게 가입신청 보낸 크루 리스트
    if type == 'invite' :
        query = CrewInvite.objects.filter(user=user,user_accept=False)
    
    #유저가 가입신청한 크루 리스트 
    elif type == 'sign' :
        query = CrewInvite.objects.filter(user=user,user_accept=True)

    serializer = UserInviteListSerializer(query, many = True)
    return Response(serializer.data)


#유저가 크루 초대 승인하기 
@api_view(['POST'])
def AcceptCrewView(request,crew_pk) :
    crew = Crew.objects.get(crew_pk=crew_pk)
    user = request.user

    #크루에 이미 가입되어 있으면 
    if crew.crew_member.filter(user_pk=user.user_pk).exists() :
        return JsonResponse({'message':"You are already a member of the crew."},status=status.HTTP_400_BAD_REQUEST)

    #아니면 크루 가입
    obj = CrewInvite.objects.get(crew=crew,user=user,crew_leader_accept=True) 
    if obj :
        crew.crew_member.add(user) 
        obj.delete() 
        Notification.objects.create(type='crew',user=user,content=f'{user.nickname}이 {crew.crew_name}크루에 가입되었습니다.',redirect_pk=crew_pk)
        data = {
            'message':f"{user.nickname}님이 {crew.crew_name}에 가입하셨습니다."
        }
        return JsonResponse(data)
    else :
        data = {
            'message':"Error"
        }
        return JsonResponse(data)

#유저가 크루 초대 거절하기
@api_view(['POST'])
def DenyCrewView(request,crew_pk) :
    crew = Crew.objects.get(crew_pk=crew_pk)
    user = request.user

    #크루에 이미 가입되어 있으면 
    if crew.crew_member.filter(user_pk=user.user_pk).exists() :
        return JsonResponse({'message':"You are already a member of the crew."},status=status.HTTP_400_BAD_REQUEST)

    # 아니면 크루 요청 거절 
    # crew.crew_member.add(user) 
    obj = CrewInvite.objects.get(crew=crew,user=user,crew_leader_accept=True) 
    if obj :
        obj.delete() 
        data = {
            'message':f"{user.nickname}님이 {crew.crew_name}의 가입 요청을 거절했습니다."
        }
        return JsonResponse(data)
    else :
        data = {
            'message':"Error"
        }
        return JsonResponse(data)

@api_view(['POST'])
def CrewLeaveAPIView(request,crew_pk) :

    crew = Crew.objects.get(crew_pk=crew_pk)
    if not crew.crew_member.filter(user_pk=request.user.user_pk).exists() :
        return JsonResponse({'message':"You are not in a crew."},status=status.HTTP_400_BAD_REQUEST)

    crew.crew_member.remove(request.user)

    return Response(status=status.HTTP_204_NO_CONTENT)

class CrewChatApiView(ListCreateAPIView) :
    serializer_class = CrewChatSerializer
    queryset = CrewChat.objects.all()
    lookup_field = 'crew_pk'

    def list(self, request, crew_pk, *args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_pk)
        queryset = CrewChat.objects.filter(crew=crew)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request, crew_pk,*args, **kwargs):
        crew = Crew.objects.get(crew_pk=crew_pk)
        if request.user in crew.crew_member.all() :
            serializer = self.get_serializer(data=request.data)
           #print(request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(crew_pk,serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else :
            return Response({'message':"You do not have permission to create the article in crew ,try again"},status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, crew_pk,serializer):
        crew = Crew.objects.get(crew_pk=crew_pk)
        serializer.save(user=self.request.user,crew=crew)
        return serializer.data