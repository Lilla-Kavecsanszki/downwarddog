from . import views
from django.urls import path

urlpatterns = [
    path('articles/', views.PostList.as_view(), name='articles'),
    path('', views.home, name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('yoga/', views.yoga_classes, name='yoga'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='articles_detail'),

]
