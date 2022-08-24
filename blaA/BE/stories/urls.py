
from stories import views
from django.urls import path

app_name='stories'
urlpatterns=[
    path('',views.story_list_or_create),
    path('follow/',views.follow_story_list),
    path('region/', views.story_region_filter),
    path('category/', views.story_category_filter),
    path('both/',views.story_both_filter),
    path('<int:story_pk>/',views.story_detail_or_update_or_delete),
    path('comment/<int:story_pk>/',views.comment_list_or_create),
    path('comment/ud/<int:comment_pk>/',views.comment_update_or_delete),
    path('hashtag/<int:story_pk>/',views.hashtag_list_or_create),
    path('hashtag/ud/<int:hashtag_pk>/',views.hashtag_update_or_delete),
    path('hashtag/filter/',views.hashtag_filter),
    path('like/<int:story_pk>/', views.like_story),
    path('mystory/<int:user_pk>/', views.mystory_list),
] 