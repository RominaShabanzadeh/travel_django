from django.urls import path,include

from travel.views import *

urlpatterns=[
    path('index/',index),
    path('create/',create_travel,name='create_travel')
]