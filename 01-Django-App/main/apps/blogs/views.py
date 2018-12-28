from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# '/' route
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

# '/new' route
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

# '/create' route
def create(request):
    return redirect('/blogs')

# '/{{ number }}
def show(request, number):
    respone = "placeholder to display blog "+ str(number)
    return HttpResponse(respone)

# '/{{ number }}/edit
def edit(request, number):
    response = "placeholder to edit blog "+ str(number)
    return HttpResponse(response)

# '/{{ number }}/delete
def destroy(request, number):
    return redirect('/blogs')
