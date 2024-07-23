from django.urls import path
from .views import *

urlpatterns = [
    path('firstbot',FirstBot),
    path('secondbot',bot2nd),
    path('test',testing),
]
