from django.urls import path
from mi.views import *
urlpatterns = [
    path('capten/',capten,name='capten')
]