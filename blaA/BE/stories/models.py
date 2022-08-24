from django.db import models

# Create your models here.

class Story(models.Model) :
    story_pk = models.AutoField(primary_key=True)
    user_pk = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    story_title = models.CharField(max_length=50)
    story_picture = models.ImageField(upload_to='user/story/')
    created_at = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    
    like_user = models.ManyToManyField('accounts.User', related_name='like_story')
    
class Comment(models.Model) :
    comment_pk = models.AutoField(primary_key=True)
    user_pk = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    story_pk = models.ForeignKey('Story', on_delete=models.CASCADE)
    story_comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Hashtag(models.Model) :
    hashtag_pk = models.AutoField(primary_key=True)
    user_pk = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    story_pk = models.ForeignKey('Story', on_delete=models.CASCADE)
    hashtag_content = models.CharField(max_length=20)
    