from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),path('ans/<str:s>/',views.ans,name='ans'),path('ans/',views.ans1,name='ans1')]
