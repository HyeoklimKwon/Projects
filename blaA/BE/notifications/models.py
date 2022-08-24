from django.db import models
from django.conf import settings
# Create your models here.
from Tracking.models import TrackingModel
class Notification(TrackingModel,models.Model):
    #프론트에 리다이렉트 시킬 유형
    type = models.CharField(max_length=20)
    #알림을 받을 유저 
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #알림 내용 
    content = models.TextField()
    #리다렉트를 위한 pk 
    redirect_pk = models.IntegerField()
    #알림 봤는지 
    view = models.BooleanField(default=False)

    