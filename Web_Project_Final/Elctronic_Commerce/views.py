from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import device,UserProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def htmll(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('Username')
        password = request.POST.get('psw')

        new_user = User.objects.create_user(name,email, password)


        new_user.save()
        return redirect('Home')
    return render(request,"Elctronic_Commerce/register.html")

def Home(request):
      if request.method == 'POST':
        name = request.POST.get('Username')
        password = request.POST.get('psw')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagetest')
        else:
            return HttpResponse('Error, user does not exist')
      return render(request,"Elctronic_Commerce/login.html")
     

def testlogin(request):
    if request.method == "POST":
        user=request.POST['user']
        return render(request,"Elctronic_Commerce/test.html",{'user':user})
    
def pagetest(request):
    devices = device.objects.all()
    return render(request, 'Elctronic_Commerce/show.html', {'devices': devices})
  


def Add(request):
    devicess = device.objects.all()
    if request.method == 'POST':
        laptopType = request.POST['laptopType']
        price = request.POST['price']
        briefDescription = request.POST['briefDescription']
        description = request.POST['description']
        
        devices = device.objects.create(laptopType=laptopType, price=price, description=description ,briefDescription=briefDescription)
        devices.save()
        return render(request,'Elctronic_Commerce/show.html',{"devices":devicess})

        
    
def AssestADD(request):
    return render(request,'Elctronic_Commerce/page.html')


def update_device(request, pk):
    devices = get_object_or_404(device, pk=pk)
    if request.method == 'POST':
        devices.laptopType = request.POST['laptopType']
        devices.price = request.POST['price']
        devices.description = request.POST['description']
        devices.briefDescription = request.POST['briefDescription']
        devices.save()
        return redirect('pagetest')
    else:
        return render(request, 'Elctronic_Commerce/update_device.html', {'device': devices})


def showFull(request, pk):
    devices = get_object_or_404(device, pk=pk)
    return render(request, 'Elctronic_Commerce/showFull.html', {'device': devices})

def Assestupdate(request):
    return render(request,'Elctronic_Commerce/update_device.html')


def add_device(request, pk):
    devices = get_object_or_404(device, pk=pk)
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    user_profile.devices.add(devices)
    return redirect('my_devices')
    
def my_devices(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    devices = user_profile.devices.all()
    return render(request, 'Elctronic_Commerce/my_devices.html', {'devices': devices})