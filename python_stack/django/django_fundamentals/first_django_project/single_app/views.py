from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return HttpResponse(index(request))

def show(request, my_val):
    return HttpResponse(f"placeholder to display blog number: {my_val}")

def edit(request, my_val):
    return HttpResponse(f"placeholder to edit blog number: {my_val}")

def destroy(request, my_val):
    return HttpResponse(index(request))