
from blacklists import views
from django.urls import path

app_name='blacklists'
urlpatterns = [
    path('',views.BlacklistAPIView.as_view()),
]
