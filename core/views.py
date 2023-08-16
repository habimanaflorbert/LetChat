from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def login_auth(request):
    return render(request,'core/login.html')

def singup(request):
    if request.method=='POST':
        form=UserAccountForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=UserAccountForm()
    return render(request,'core/singup.html',{'form':form})
    
def home(request):
    return render(request,'core/base.html') 