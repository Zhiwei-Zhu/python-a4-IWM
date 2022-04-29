from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createroom', views.createroom, name='createroom'),
    path('<room_name>/', views.room, name='room'),
]