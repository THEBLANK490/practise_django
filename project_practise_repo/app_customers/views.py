from django.shortcuts import render

# Create your views here.
def create (request):
    return render(request,"/customers.create.html")

def edit (request):
    return render(request,"/customers.edit.html")

def index (request):
    return render(request,"/customers.index.html")

def show (request):
    return render(request,"/customers.show.html")
