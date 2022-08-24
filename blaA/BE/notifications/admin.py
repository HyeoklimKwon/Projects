from django.contrib import admin

from notifications.models import Notification

# Register your models here.

class NotiAdmin(admin.ModelAdmin) :
    list_display = ('type','content','view')

admin.site.register(Notification,NotiAdmin)