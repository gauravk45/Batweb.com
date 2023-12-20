from django.shortcuts import render
from .models import Member

def home(request):
    all_member=Member.objects.all
    return render(request,'home.html',{'all':all_member})

def join(request):
    return render(request,'join.html',{})
