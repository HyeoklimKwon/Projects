import json
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from reviews.models import ButtonReview, Store,Review, StoreButtonReview
from reviews.serializers.review import ReviewDetailtSerializer, ReviewListCreateSerializer, ReviewShortListSerializer
from reviews.serializers.store import StoreListCreateSerializer
from rest_framework import filters
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Count 
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated



#리뷰를 작성할 가게 검색 or 가게 추가
class StoreListCreateAPIView(ListCreateAPIView):
    #요청한 user_pk로 유저 조회 
    # authentication_classes=[]
    serializer_class = StoreListCreateSerializer
    filter_backends = [filters.SearchFilter]
    queryset=Store.objects.all()
    search_fields = ['name']


class ReviewListAPIView(ListAPIView) :
    authentication_classes=[]
    serializer_class = ReviewListCreateSerializer
    filter_backends = [filters.SearchFilter]
    queryset = Review.objects.all()


#가게에 달린 리뷰 전체조회 및 리뷰 생성
class StoreReviewListCreateAPIView(ListCreateAPIView) :
    # authentication_classes=[]
    serializer_class = ReviewListCreateSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['created_at']


    queryset = Review.objects.all()

    def get_object(self, store_pk):
        try:
            return Store.objects.get(pk=store_pk)
        except Store.DoesNotExist:
            raise Http404

    def review_store(self,store_pk,review_pk,chosen_button) :
        store = get_object_or_404(Store,store_pk=store_pk)
        review = get_object_or_404(Review,review_pk=review_pk)
        for choice in chosen_button :
            # choice = int(choice)
            btn = get_object_or_404(ButtonReview,pk=choice)
            StoreButtonReview.objects.create(store=store,button=btn,review=review)

    def review_button_aggregate(self,store_pk) :
        store = get_object_or_404(Store,store_pk=store_pk)
        cnt = store.review.count()
        tmp = {'친절한 사장님': 0,'깨끗한 매장':0 ,'좋은 분위기':0,'교통 접근성':0,'칼퇴근 가능':0,'유니폼 제공':0}
        if cnt :
            for button_review in store.storebuttonreview_set.all() :
                tmp[button_review.button.type] += 1 

            for btn in tmp :
                tmp[btn] = int(round(tmp[btn]/cnt,2)*100)
        return tmp

    def review_star_aggregate(self,store_pk) :
        store = get_object_or_404(Store,store_pk=store_pk)
        cnt = store.review.count()

        if cnt :
            review = Review.objects.filter(store=store).aggregate(Sum('star'))
            # sum = Store.objects.all().aggregate(Sum('star'))
            print(cnt,review)
            return round(review['star__sum']/cnt,1)
        else :
            return 0


    def list(self, request,store_pk):
        # print(request.query_params['ordering'])
        queryset = self.filter_queryset(Review.objects.filter(store=self.get_object(store_pk)))
        queryset = queryset.annotate(like_user_count=Count('like_users'))
        if request.query_params :
            if request.query_params['ordering'] == '-like_user_count':
                queryset = queryset.order_by('-like_user_count')
            elif request.query_params['ordering'] == 'like_user_count' :
                queryset = queryset.order_by('like_user_count')
        serializer = ReviewShortListSerializer(queryset,many=True)
        # update_data = {'review_static':self.button_review_aggregate(store_pk)}
        review_button_satic = {'review_button_static':self.review_button_aggregate(store_pk)}
        review_star_satic = {'review_star_static' : self.review_star_aggregate(store_pk)}
        response_data = serializer.data
        response_data.append(review_button_satic)
        response_data.append(review_star_satic)
        # update_data.update(serializer.data)
        return Response(response_data)

    def create(self,request,store_pk) : 
        # chosen_button = request.data.pop('chosen_button')
        # print(chosen_button)

        reviews = Review.objects.filter(store=store_pk,user=self.request.user)
        if reviews :
           return Response({'message':"Sorry, You can only write a review for a store once per user."},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer,store_pk)
        headers = self.get_success_headers(serializer.data)
        review_pk = serializer.data['review_pk']
        chosen_button = request.data.pop('chosen_button')
        try :
            chosen_button = list(map(int,chosen_button))
            self.review_store(store_pk,review_pk,chosen_button)
            update_data = {'chosen_button' : list(chosen_button)}
            update_data.update(serializer.data)
            return Response(update_data, status=status.HTTP_201_CREATED, headers=headers)
        except :
            return Response({'message':"Sorry, Wrong button review."},status=status.HTTP_400_BAD_REQUEST)
        # print(list(chosen_button))

    def perform_create(self, serializer,store_pk):
        return serializer.save(user=self.request.user,store=self.get_object(store_pk))

@api_view(['POST'])
def review_like(request,review_pk) :
    review = get_object_or_404(Review,review_pk=review_pk)
    user = request.user 
    
    if review.like_users.filter(pk=user.user_pk).exists() :
        review.like_users.remove(user)
        serializer = ReviewShortListSerializer(review)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else :
        review.like_users.add(user)
        serializer = ReviewShortListSerializer(review)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

class ReviewDetailDelteAPIView(RetrieveDestroyAPIView) :

    # authentication_classes=[]
    serializer_class = ReviewDetailtSerializer
    queryset = Review.objects.all()
    # permission_classes = (IsAuthenticated)
    lookup_field='review_pk'

    def retrieve(self, request,review_pk, *args, **kwargs):
        instance = self.get_object()
        review = Review.objects.get(review_pk=review_pk)
        btn_review = review.storebuttonreview_set.all()
        tmp_button ={'친절한 사장님': 0,'깨끗한 매장':0 ,'좋은 분위기':0,'교통 접근성':0,'칼퇴근 가능':0,'유니폼 제공':0}
        for btn in btn_review :
            # tmp_btn  = get_object_or_404(ButtonReview, pk=btn.button.pk)
            # print(tmp_btn)
            tmp_button[btn.button.type]+=1
        print(tmp_button)
        serializer = self.get_serializer(instance)
        response_data = serializer.data
        # response_data.add(button_review)
        btn_review = {"button":tmp_button}
        btn_review.update(response_data)
        return Response(btn_review)



