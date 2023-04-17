from django.urls import path
from . import views


urlpatterns = [
    path('addpost', views.AddPost, name= 'addpost'),
    path('addquestion', views.AddQuestion, name= 'addquestion'),
    path('allpost', views.allpost, name= 'allpost'),
    path('allque', views.allque, name= 'allque'),
    path('update/<int:id>', views.update, name= 'update'),
    path('delete/<int:id>', views.delete, name= 'delete'),
]