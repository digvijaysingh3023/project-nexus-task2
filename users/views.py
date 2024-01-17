from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'users/home.html')
def login_(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            # messages.success(request,'Login Successful')
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Wrong Credentials! Try again')
            return redirect('login')
    
    return render(request,'users/login.html')
        

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['confirmpassword']
        newuser=User.objects.create_user(username = username,password=pass1)
        newuser.save()
        
        messages.success(request,f"Account created successfully for {username} .You can now login.")
        return redirect('login')
    
    return render(request, 'users/register.html')


def success(request):
    return render(request,'users/success.html')

def logout_(request):
    user = request.user
    logout(request)

    return redirect('home')
