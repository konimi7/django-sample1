from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World")

def foo(request):
    return HttpResponse("Foo")

def woo(request):
    return HttpResponse("Woo")
