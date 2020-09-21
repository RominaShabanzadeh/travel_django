from django.urls import path,include

from travel.views import *

urlpatterns=[
    path('index/',index),
    path('create/',create_travel,name='create_travel'),
    path('',include('django.contrib.auth.urls'),name='login'),
    path('register/',register,name='register')
]