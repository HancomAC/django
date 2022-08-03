from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
]

app_name = 'blog'