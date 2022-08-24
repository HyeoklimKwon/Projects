from categorys import views
from django.urls import path,include


app_name='categorys'
urlpatterns=[
    path('region/',views.SidoListAPIView.as_view(),name='sido'),
    path('region/<int:sido>/',views.GugunListAPIView.as_view(),name='gugun'),
    path('region/<int:sido>/<int:gugun>/',views.DongListAPIView.as_view(),name='dong'),
    path('job/',views.JobListAPIView.as_view(),name='job'),
]