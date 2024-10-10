from django.urls import path
from rcb.views import *
urlpatterns = [
    path('capten/',capten,name='capten')
]