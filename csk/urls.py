from django.urls import path
from csk.views import *
urlpatterns = [
    path('capten/',capten,name='capten'),
    path('viscap/',viscap,name='viscap'),
]