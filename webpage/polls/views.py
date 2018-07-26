from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 主页
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

