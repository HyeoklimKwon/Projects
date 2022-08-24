from django.db import models
#Django 
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import jwt
from datetime import datetime, timedelta

from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser) :

#------------사용하지 않을 기본 상속 필드 ------------------------------
    username = None
    first_name = None
    last_name = None
    last_login = None
    groups = None
    date_joined = None


#-------------사용할 필드 ---------------------------------------
    user_pk = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'),unique=True)
    tel = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20,unique=True)
    region = models.TextField(null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    is_alba = models.BooleanField(default=0)
    image = models.ImageField(upload_to='user/profile/',
                default='user/profile/profile_default1.png',
                null=True,blank=True)
    report = models.IntegerField(default=0)
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers',blank=True)
#---------------email을 기본 필드로 생성 -------------------------------------
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tel','name','nickname']
    objects = CustomUserManager()
    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now( ) + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

    def __str__(self) :
        return self.email