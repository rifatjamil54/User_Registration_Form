from django.shortcuts import render
from .forms import SingUpForm
# Create your views here.

def sign_up(request):
    
    if request.method == 'POST':
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:        
        fm = SingUpForm()

    return render(request,'enrool/sign_up.html',{'form':fm})
