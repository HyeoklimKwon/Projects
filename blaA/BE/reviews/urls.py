from reviews import views
from django.urls import path,include


app_name='reviews'
urlpatterns=[
    path('store/',views.StoreListCreateAPIView.as_view(),name='store'),
    # path('',views.ReviewListAPIView.as_view(),name='review'),
    path('<int:store_pk>/',views.StoreReviewListCreateAPIView.as_view(),name='review_create'),
    path('like/<int:review_pk>/',views.review_like,name='review_like'),
    path('detail/<int:review_pk>/',views.ReviewDetailDelteAPIView.as_view(),name='review_datail'),
    # path('search_store/',views.StoreListAPIView.as_view(),name='store_search'),
]