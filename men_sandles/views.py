from django.shortcuts import render
from django.http import HttpResponse
from .models import Product



# Create your views here.
def msandles(request):
      
      ns=request.session.get('user_name',None)
      products = Product.objects.all()
      
     
      return render(request,'msandles.html',{'username':ns,'products': products})


      


