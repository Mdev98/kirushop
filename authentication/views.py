from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from authentication import forms

# Create your views here.

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'authentication/register_page.html', context={'form':form})

def login_user(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            user = authenticate(identifier=form.cleaned_data['identifier'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'authentication/login_page.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def change_user_password(request):
    form = forms.ChangePasswordForm()
    if request.method == 'POST':
        form = forms.ChangePasswordForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['old_password'])
            if user is not None:
                new_password = make_password(form.cleaned_data['new_password'])
                user.password = new_password
                user.save()
                return redirect('home')
    return render(request, 'authentication/change_password_page.html', context={'form': form})