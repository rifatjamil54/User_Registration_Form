from django.shortcuts import render, HttpResponseRedirect
from .forms import SingUp_Forms, UserEditForms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.


def singup_page_rendering(request):
    if request.method == 'POST':
        singup_form = SingUp_Forms(request.POST)
        if singup_form.is_valid():
            name = singup_form.cleaned_data['first_name']
            singup_form.save()
            messages.success(request,f'Congratulation! {name}, Your Account Created. Please Login.')
    else:
        singup_form = SingUp_Forms()    
    return render(request, 'registration_app/singup.html',{'singup_form':singup_form})


def login_page_rendering(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                form_username = login_form.cleaned_data['username']
                form_passwoed = login_form.cleaned_data['password']
                user = authenticate(username = form_username, password = form_passwoed)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Your Account logged in successfully!!')
                    return HttpResponseRedirect('/registration_app/profile/')
        else:
            login_form = AuthenticationForm()
        return render(request,'registration_app/login.html',{'login_form':login_form})
    else:
        return HttpResponseRedirect('/registration_app/profile/')


def profile_page_rendering(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserEditForms(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, "Profile Update!")
                fm.save()
        else:        
            fm = UserEditForms(instance=request.user)
        return render(request,'registration_app/profile.html', {'name':request.user, 'form':fm})    
    else:
        messages.success(request,'Please login first!')
        return HttpResponseRedirect('/registration_app/login/')


def logout_profile(request):
    logout(request)
    return HttpResponseRedirect('/registration_app/login/')

def changing_password(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password changed successfully!')
                return HttpResponseRedirect('/registration_app/login/')
        else:
            fm = PasswordChangeForm(user=request.user)        
        return render(request, 'registration_app/changing_password.html',{'forms':fm}) 
    else:
        messages.success(request,'Please login first!')
        return HttpResponseRedirect('/registration_app/login/')
