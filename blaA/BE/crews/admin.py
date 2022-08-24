from django.contrib import admin
from crews.models import CrewInvite

from crews.models import Crew, CrewArticle, CrewArticleComment, CrewArticleImage, CrewSchedule

# Register your models here.
admin.site.register(Crew)
admin.site.register(CrewArticle)
admin.site.register(CrewArticleImage)
admin.site.register(CrewArticleComment)
admin.site.register(CrewSchedule)
admin.site.register(CrewInvite)