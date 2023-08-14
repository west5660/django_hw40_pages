from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world</h1>')

def about(request):
    return HttpResponse('<b> О нашей фирме</b>')

def index1(request):
    return render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')

def contacts(request):
    return render(request, 'contacts.html')

def workers(request):
    return render(request, 'workers.html')