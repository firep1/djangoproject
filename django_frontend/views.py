from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homepage(request):
    context = {'class1': 'active'}   #context ma active class pass gareko in each html request
    return render(request,"home.html",context)

@login_required(login_url='login')
def about(request):
    context = {'class4': 'active'}
    return render(request,"about.html",context)

@login_required(login_url='login')
def predict(request):
    context = {'class2': 'active'}
    return render(request,"predict.html",context)

def loginpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect")
    
    context = {'class3': 'active'}
    return render(request,"login.html",context)

def logoutpage(request):
    logout(request)
    return redirect('login')
