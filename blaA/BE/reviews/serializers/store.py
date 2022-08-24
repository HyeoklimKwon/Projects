from rest_framework import serializers
from reviews.models import Review
from reviews.models import Store
from django.db.models import Sum
class StoreListSerializer(serializers.ModelSerializer) :
    star = serializers.SerializerMethodField()
    button = serializers.SerializerMethodField()

    def get_star(self,obj) :
        cnt = obj.review.count()
        if cnt :
            review = Review.objects.filter(store=obj).aggregate(Sum('star'))

            return round(review['star__sum']/cnt,1)
        else :
            return 0
    
    def get_button(self,obj) :
        cnt = obj.review.count()
        tmp = {'친절한 사장님': 0,'깨끗한 매장':0 ,'좋은 분위기':0,'교통 접근성':0,'칼퇴근 가능':0,'유니폼 제공':0}
        if cnt :
            for button_review in obj.storebuttonreview_set.all() :
                tmp[button_review.button.type] += 1 

            for btn in tmp :
                tmp[btn] = int(round(tmp[btn]/cnt,2)*100)
        return tmp

    class Meta : 
        model = Store
        fields = '__all__'

class StoreNoneImageCreateSerializer(serializers.ModelSerializer) :

    class Meta : 
        model = Store
        fields = '__all__'
    
    def create(self, validated_data):
        instance = Store.objects.create(**validated_data)
        if '맥주' in instance.name :
            if '역전할머니맥주' in instance.name : 
                instance.image = 'store/logo/역전할머니맥주.jpg'
            else : 
                instance.image = 'store/logo/맥주.png'
        elif '스타벅스' in instance.name : 
            instance.image = 'store/logo/스타벅스.jpeg'
        elif '메가커피' in instance.name : 
            instance.image = 'store/logo/메가커피.png'
        elif '버거킹' in instance.name : 
            instance.image = 'store/logo/버거킹.jpg'
        elif '빽다방' in instance.name : 
            instance.image = 'store/logo/빽다방.jpeg'
        elif '서브웨이' in instance.name : 
            instance.image = 'store/logo/서브웨이.jpg'
        elif '아임일리터' in instance.name : 
            instance.image = 'store/logo/아임일리터.png'
        elif '이디야' in instance.name : 
            instance.image = 'store/logo/이디야.jpeg'
        elif '투썸플레이스' in instance.name : 
            instance.image = 'store/logo/투썸플레이스.png'

        instance.save()
        return instance

class StoryCreateSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Store
        fields = ('store_pk','name','image','region')