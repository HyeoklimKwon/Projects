from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from crews.models import Crew
from crews.serializer.crew import CrewListSerializer
from reviews.models import Review
# 모델 시리어라이저를 상속받는 이유는 이미 모델이 있기 때문이다.
class RegisterSerializer(serializers.ModelSerializer) :
    password = serializers.CharField(max_length=128,min_length=6,write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta() :
        model=User
        fields= ('user_pk','email','password','tel','name','nickname','region','category','is_alba','token','image')
        read_only_fields = ['image']
    def create(create,validated_data) :

        return User.objects.create_user(**validated_data)
    

class LoginSerializer(serializers.ModelSerializer) :
    
    password = serializers.CharField(max_length=128,min_length=6,write_only=True)
    
    class Meta() :
        model=User
        fields = ('user_pk','email','password','token',)
        
        read_only_fields = ['token']

class UserListSerializer(serializers.ModelSerializer) :
        
    class Meta :
        model=User
        fields = ('user_pk','image','nickname')
        

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.IntegerField(source = 'followers.count',read_only=True)
    followings = serializers.IntegerField(source = 'followings.count',read_only=True)
    class Meta:
        model = User
        fields= ['user_pk','email','name','nickname','region','category','is_alba','image','followers','followings','tel','image']
        read_only_fields = ['email']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.region = validated_data.get('region', instance.region)
        instance.category = validated_data.get('category', instance.category)
        instance.is_alba = validated_data.get('is_alba', instance.is_alba)

        try:
            images_data = validated_data.get('image')
        except:
            images_data = None
        # print(validated_data.get())
        if images_data is not None:
            instance.image = images_data

        instance.save()

        return instance

class UserNoneImageSerializer(serializers.ModelSerializer):
    followers = serializers.IntegerField(source = 'followers.count',read_only=True)
    followings = serializers.IntegerField(source = 'followings.count',read_only=True)
    class Meta:
        model = User
        fields= ['user_pk','email','name','nickname','region','category','is_alba','image','followers','followings','tel','image']
        read_only_fields = ['email','image']
        

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance



class EmailUniqueCheckSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('email',)
        
 # 닉네임 중복 검사
class NicknameUniqueCheckSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(required=True, min_length=1, max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('nickname',)

class UserCrewSerializer(serializers.ModelSerializer):
    
    crews = CrewListSerializer(many=True)
    class Meta:
        model = User
        fields= ('user_pk','crews')


class ReviewSerializer(serializers.ModelSerializer) :
    store_pk = serializers.IntegerField(source='store.store_pk')
    store_name = serializers.CharField(source='store.name')
    store_image = serializers.ImageField(source='store.image')
    class Meta: 
        model = Review
        fields = ('review_pk','user','star','store_pk','store_name','store_image')
        

class UserReviewSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = User
        fields= ('user_pk','reviews')
        