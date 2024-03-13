from django.urls import path
from .views import *

urlpatterns = [
    path('firstbot',FirstBot),
    path('test',testing),
]
