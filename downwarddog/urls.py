from . import views
from django.urls import path

urlpatterns = [
    path('articles/', views.PostList.as_view(), name='articles'),
    path('', views.home, name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('yoga/', views.YogaList.as_view(), name='yoga'),
    path('articles/<slug:slug>/', views.PostDetail.as_view(), name='articles_detail'),
    path('yoga/<slug:slug>/', views.YogaDetail.as_view(), name='yoga_detail'),
    path('book-now/<int:timetable_id>/',
         views.BookNow.as_view(), name='book_now'),
    path('my-bookings/', views.MyBookings.as_view(), name='my_bookings'),
    path('my-bookings/<int:booking_id>/',
         views.MyBookings.as_view(), name='delete_booking'),
]
