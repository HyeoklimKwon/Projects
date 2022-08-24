from django.contrib import admin
from crews.models import CrewInvite

from crews.models import Crew, CrewArticle, CrewArticleComment, CrewArticleImage, CrewSchedule


class CrewAdmin(admin.ModelAdmin):
    list_display = ('crew_pk', 'crew_leader', 'crew_name',)

# Register your models here.
admin.site.register(Crew,CrewAdmin)

class CrewArticleAdmin(admin.ModelAdmin) :
    list_display = ('crew_article_pk','crew_title')

admin.site.register(CrewArticle,CrewArticleAdmin)


admin.site.register(CrewArticleImage)
admin.site.register(CrewArticleComment)

class CrewScheduleeAdmin(admin.ModelAdmin) :
    list_display = ('crew','user','crew_day')

admin.site.register(CrewSchedule,CrewScheduleeAdmin)

class CrewInviteAdmin(admin.ModelAdmin) :
    list_display = ('crew','user','crew_leader_accept','user_accept')


admin.site.register(CrewInvite,CrewInviteAdmin)