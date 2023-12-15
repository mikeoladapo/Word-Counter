from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , 'home.html')

def count(request):
    text = request.POST['words']
    count= len(text.split())
    return render(request,'count.html',{'counter':count})

    

# Create your views here.
