from django.contrib import admin
from stories.models import Comment, Hashtag

from stories.models import Story

# Register your models here.

class StoryAdmin(admin.ModelAdmin) :
    list_display = ('story_pk','story_title')

admin.site.register(Story,StoryAdmin)

class CommentAdmin(admin.ModelAdmin) :
    list_display = ('comment_pk','story_comment')
admin.site.register(Comment,CommentAdmin)

class HashtagAdmin(admin.ModelAdmin) :
    list_display= ('hashtag_pk','hashtag_content')

admin.site.register(Hashtag)