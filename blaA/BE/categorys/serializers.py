from rest_framework import serializers

from categorys.models import Dong, Gugun, JobCategory, Sido


class SidoSerializer(serializers.ModelSerializer) :
    
    
    class Meta() :
        model=Sido
        fields = '__all__'
        

class GugunSerializer(serializers.ModelSerializer) :
    
    
    class Meta() :
        model=Gugun
        fields = '__all__'
        
class DongSerializer(serializers.ModelSerializer) :
    
    
    class Meta() :
        model=Dong
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer) :
    
    
    class Meta() :
        model=JobCategory
        fields = '__all__'
        