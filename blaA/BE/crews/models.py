from django.db import models
from Tracking.models import TrackingModel
from django.conf import settings
# Create your models here.

class Crew(TrackingModel,models.Model) :
    crew_pk = models.AutoField(primary_key=True)
    crew_leader = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_business = models.BooleanField()
    crew_name = models.CharField(max_length=50,unique=True)
    crew_img = models.ImageField(upload_to='crew/image',
                default='crew/image/상점기본.png',
                null=True,blank=True)
    crew_explain = models.TextField()
    crew_region = models.TextField(null=True,blank=True)
    crew_member = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='crews',blank=True)

    

class CrewArticle(TrackingModel,models.Model) :
    crew_article_pk = models.AutoField(primary_key=True)
    crew = models.ForeignKey(Crew,on_delete=models.CASCADE) 
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    crew_title = models.CharField(max_length=50)
    crew_content = models.TextField()
    crew_private = models.BooleanField(default=False)
    crew_pin = models.BooleanField(default=False)


class CrewArticleImage(models.Model) :
    article_image_pk = models.AutoField(primary_key=True)
    article =models.ForeignKey(CrewArticle,on_delete=models.CASCADE)
    article_picture = models.ImageField(upload_to='crew_article/image')

    def __str__(self) :
        return str(self.article_picture)

class CrewArticleComment(TrackingModel,models.Model) :
    crew_comment_pk = models.AutoField(primary_key=True)
    crew = models.ForeignKey(Crew,on_delete=models.CASCADE) 
    article =models.ForeignKey(CrewArticle,on_delete=models.CASCADE)
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comment_content = models.TextField()

class CrewInvite(models.Model) :
    crew = models.ForeignKey(Crew,on_delete=models.CASCADE) 
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    crew_leader_accept = models.BooleanField()
    user_accept = models.BooleanField()
    
class CrewSchedule(models.Model) :
    crew_schedule_pk = models.AutoField(primary_key=True)
    crew = models.ForeignKey(Crew,on_delete=models.CASCADE)
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    crew_day = models.DateField()
    color = models.CharField(max_length=20)
    crew_starthour = models.TimeField()
    crew_endhour = models.TimeField()
    
class CrewChat(TrackingModel,models.Model) :
    chat_pk = models.AutoField(primary_key=True)
    crew = models.ForeignKey(Crew,on_delete=models.CASCADE)
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()

    


    