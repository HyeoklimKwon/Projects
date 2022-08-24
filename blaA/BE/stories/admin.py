from django.contrib import admin
from stories.models import Comment, Hashtag

from stories.models import Story

# Register your models here.
admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Hashtag)