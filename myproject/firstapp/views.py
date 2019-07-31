from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')

def faq(request):
    return render(request,'faq.html')

def qna(request):
    return render(request,'qna.html')

def notice(request):
    return render(request,'notice.html')