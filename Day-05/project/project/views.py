from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")

def aboutUs(request):
    return render(request,"aboutUs.html")

def course(request):
    return render(request,"course.html")

def contact(request):
    return render(request,"contact.html")

def resume(request):
    return render(request,"resume.html")