from django.urls import path
from . import views


urlpatterns = [
    path('addpost', views.AddPost, name= 'addpost'),
    path('addquestion', views.AddQuestion, name= 'addquestion'),
    path('allpost', views.allpost, name= 'allpost'),
    path('allque', views.allque, name= 'allque'),
]