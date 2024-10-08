from django.urls import path
from feed import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-post/', views.create_post, name="create_post"),
    path('post-comment/', views.post_comment, name="post_comment"),
    path('explore/', views.explore, name="explore"),
    path('profiles/', views.explore_profiles, name="explore_profiles"),
    path('search/', views.search, name="search"),
    path('notifications/', views.notifications, name="notifications"),
    path('like-post/', views.post_like, name="like_post"),
]
