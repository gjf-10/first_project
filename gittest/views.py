from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index():
    print('my first pycharm-git')
    return HttpResponse('OK')