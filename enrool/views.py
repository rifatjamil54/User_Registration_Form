from django.shortcuts import render, HttpResponseRedirect
from .forms import SingUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.



def user_signup(request):
    if request.method == 'POST':
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Successfully')
            fm.save()
    else:        
        fm = SingUpForm()
    return render(request,'enrool/sign_up.html',{'form':fm})



def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password= upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')                
        else:
            fm = AuthenticationForm()
        return render(request,'enrool/login_file.html',{'form':fm})



def user_profile(request):

    if request.user.is_authenticated:
        return render(request,'enrool/profile.html',{'name': request.user})
    else:
        return HttpResponseRedirect('/login/')



def user_logout(request):

    logout(request)

    return HttpResponseRedirect('/login/')



# with old password
def user_change_pass(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully!')
                return HttpResponseRedirect('/profile/')
        else:    
            fm = PasswordChangeForm(user = request.user)
        return render(request,'enrool/changepass.html',{'form':fm}) 

    else:
        return HttpResponseRedirect('/login/')



