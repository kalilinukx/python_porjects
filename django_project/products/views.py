from django.shortcuts import render
from django.shortcuts import HttpResponse
# uniform recourse locator


def index(request):
    return HttpResponse("Hello World")


def new(request):
    return HttpResponse('new products')


def hello(request):
    return HttpResponse("this is going to be a hello introduction")