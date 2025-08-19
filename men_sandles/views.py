from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def msandles(request):
      
      ns=request.session.get('user_name',None)
     
      return render(request,'msandles.html',{'username':ns})


      


