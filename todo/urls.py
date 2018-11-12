from django.urls import path
from . import views
#현재폴더에 있는 views 파일 추가
urlpatterns=[
    path('',views.index),
    path('new/',views.new),
    path('create/',views.create),
    ]