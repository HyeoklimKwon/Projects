from notifications import views
from django.urls import path

app_name='notifications'
urlpatterns=[
    path('',views.NotificationListAPIView.as_view(),name='notification'),
    path('<int:pk>',views.NotificationDestoryAPIView.as_view(),name='delete'),
    ] 