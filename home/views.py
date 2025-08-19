from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def hom(request):
  #  return render(request,'home.html')

def homes(request):
    ns=request.session.get('user_name',None)
    return render(request,'main.html',{'msg':ns})

def h(request):
    return render(request,'new.html')

