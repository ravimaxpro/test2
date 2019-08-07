from django.shortcuts import render
from django.http import HttpResponse

def input(request):
    return render(request,'input.html')

def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    request.session['z']=z
    request.session.set_expiry(60)
    return HttpResponse('data submitted')

def display(request):
    if request.session.has_key('z'):
        z=request.session['z']
        return HttpResponse(z)
    else:
        return render(request,'input.html')

# Create your views here.
