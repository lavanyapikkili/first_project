from django.shortcuts import render
from django.http import HttpResponse

def fun1(request):
    return HttpResponse ('hello')

