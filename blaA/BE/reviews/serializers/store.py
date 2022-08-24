from rest_framework import serializers
from reviews.models import Store

class StoreListCreateSerializer(serializers.ModelSerializer) :

    class Meta : 
        model = Store
        fields = '__all__'


        def create(self, validated_data):
            images_data = self.context['request'].FILES
            store = Store.objects.create(**validated_data)
            if images_data :
                store.image = images_data
            return store

