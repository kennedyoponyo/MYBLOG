from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser

# Create your views here.
def userRegistration(request):
    if request.method=='POST':
        username=request.POST.get('userId')
        email=request.POST.get('userEmail')
        firstName=request.POST.get('first_name')
        lastName=request.POST.get('last_name')
        tel=request.POST.get('phoneNo')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')

        if pass1 != pass2:
            messages.error(request,'password do not match')
            return redirect ('regist')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'username already taken')
            return redirect ('regist')
        
        myuser=CustomUser.objects.create_user(
            username=username,
            email=email,
            fname=firstName,
            lname=lastName,
            phone=tel,
            password=pass1
        )
        
        myuser.save()
        messages.success(request, 'Account created successfully')
        return redirect ('signin')
    
    return render(request,'account/regist.html')

#login view

def signin_view(request):
    if request.method=='POST':
        username=request.POST.get('userId')
        password=request.POST.get('pass1')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'login successful')
            return redirect ('home')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('signin')
        
    return render(request,'account/signin.html')
        

#logout view
 
def signout_view(request):
    logout(request)
    return redirect('signin')



