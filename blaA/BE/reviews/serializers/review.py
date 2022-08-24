from rest_framework import serializers
from reviews.models import Review, Store
from accounts.models import User


class ReviewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields= ('nickname',)


class StoreListCreateSerializer(serializers.ModelSerializer) :

    class Meta : 
        model = Store
        fields = '__all__'

class ReviewListCreateSerializer(serializers.ModelSerializer) :
    chosen_button = serializers.ListField(write_only=True)

    class Meta: 
        model = Review
        fields = '__all__'
        read_only_fields = ('user','store','like_users','chosen_button')

    def create(self,validated_data) :

        chosen_button = validated_data.pop('chosen_button')
        review = Review.objects.create(**validated_data)
        # print(store)
        return review


class ReviewShortListSerializer(serializers.ModelSerializer) :

    user = ReviewUserSerializer()
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta: 
        model = Review
        fields = ('review_pk','user','oneline_review','created_at','like_users','like_user_count')
        
class ReviewDetailtSerializer(serializers.ModelSerializer) :

    user = ReviewUserSerializer()
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta: 
        model = Review
        fields = ('review_pk','user','star','oneline_review','created_at','like_users','like_user_count')
