from rest_framework import serializers

from crews.models import Crew,CrewArticle,CrewArticleImage

class CrewSerializerForArticle(serializers.ModelSerializer) :
    class Meta: 
        model = Crew
        fields= ('crew_pk',)


class ArticleImageSerializer(serializers.ModelSerializer):
   class Meta:
      model = CrewArticleImage
      fields = ['article_image_pk','article_picture']


class CrewArticleSerializer(serializers.ModelSerializer) :
    # crew_pk = CrewSerializerForArticle()
    images = serializers.SerializerMethodField()
    def get_images(self, obj):
        image = obj.crewarticleimage_set.all()
        return ArticleImageSerializer(instance=image, many=True).data


    class Meta: 
        model = CrewArticle
        fields = '__all__'
        read_only_fields = ('crew','user','images')


    def create(self,validated_data) :
        images_data = self.context['request'].FILES 
        print(images_data)
        print(validated_data)
        article = CrewArticle.objects.create(**validated_data)
        for image_data in images_data.getlist('images'):
            CrewArticleImage.objects.create(article=article, article_picture=image_data)
        return article

    # def update(self,instance,validated_data) :
    #     instance.title = validated_data.get'

class CrewArticleRUDSerializer(serializers.ModelSerializer) :
    # crew_pk = CrewSerializerForArticle()
    images = serializers.SerializerMethodField()
    # image_update = serializers.BooleanField(write_only=True)
    def get_images(self, obj):
        image = obj.crewarticleimage_set.all()
        return ArticleImageSerializer(instance=image, many=True).data


    class Meta: 
        model = CrewArticle
        fields = '__all__'
        read_only_fields = ('crew','user','images')


    def update(self, instance, validated_data):
       
        instance.crew_title = validated_data.get('crew_title', instance.crew_title)
        instance.crew_content = validated_data.get('crew_content', instance.crew_content)
        instance.crew_private = validated_data.get('crew_private', instance.crew_private)
        instance.crew_pin = validated_data.get('crew_pin', instance.crew_pin)
        try:
            images_data = self.context['request'].FILES 
        except:
            images_data = None
        # print(validated_data.get())
        if images_data is not None:
            image_instance_list = []
            for image_data in images_data.getlist('images'):
                # print('asdf',image_data)
                # print(CrewArticleImage.objects.get(article_picture =f'crew_article/image/{image_data}'))
                image, created = CrewArticleImage.objects.get_or_create(article_id = instance.pk,article_picture=f'crew_article/image/{image_data}')
                if created :
                    image_instance_list.append(image)

            instance.crewarticleimage_set.set(image_instance_list)
        instance.save()

        return instance