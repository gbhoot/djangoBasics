from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

# Create your views here.

def index(request):
    response = "Hello, I am your first request!"

    return HttpResponse(response)

def test(request):
    response = "Hello, I am a test"

    return HttpResponse(response)
