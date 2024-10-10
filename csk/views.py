from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def capten(request):
    return render(request,'csk.html')
def viscap(request):
    return HttpResponse('hardhik')
