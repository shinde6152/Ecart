from django.shortcuts import render,redirect
from store.models.product import product
from store.models.category import category
from store.models.sign import sign

# Create your views here.

def index(request):

    return render(request,'index.html',data)


def signup(request):

    return render(request,'sign.html')

def login(request):

    return render(request,'login.html')


def logout(request):
    #
    return redirect('/')
