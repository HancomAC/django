from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_question, name='add_question'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:question_id>/add', views.add_choice, name='add_choice'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/delete', views.delete, name='delete'),
]

app_name = 'polls'
