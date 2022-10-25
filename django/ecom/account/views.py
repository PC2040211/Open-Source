from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_page(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=email)
        if not  user_obj.exists():
            messages.warning(request,'Account not found')
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request,'Your account is not verified')
            return HttpResponseRedirect(request.path_info)
        user_obj=authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        messages.warning(request,'Invalid Credentials')
        return HttpResponseRedirect(request.path_info)









    return render(request,'account/login.html')
def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=email)
        if user_obj.exists():
          messages.warning(request,'Email is already taken!!')
          return HttpResponseRedirect(request.path_info)
        user_obj=User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
        print(user_obj)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,"an email is send successfully")
        return HttpResponseRedirect(request.path_info)
    return render(request,'account/register.html')