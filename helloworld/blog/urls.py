from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('search/', views.PostSearch.as_view(), name='search'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    path('comment/', views.CommentAdd.as_view(), name='comment'),
    path('post/', views.PostAdd.as_view(), name='post'),
]

app_name = 'blog'
