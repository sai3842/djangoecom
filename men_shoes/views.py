from django.shortcuts import render
from login_sigin.views import login_view



# Create your views here.
def mshoes_view(request):
    
    
     ns=request.session.get('user_name',None)
     return render(request, 'mshoes.html', {'username': ns})
    

def show(request,no):
     

      return render(request,'new.html')

def nike_view(request):
      
      
      return render(request,'view.html')
