from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def listusers(request):
    return HttpResponse("以下是用户信息")