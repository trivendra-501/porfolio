# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import logout


def signup(request):
    if request.method == "POST":
        get_first_name = request.POST.get('first_name')
        get_last_name = request.POST.get('last_name')
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        get_dob = request.POST.get('dob')
        get_phonenumber = request.POST.get('phone')
        get_city = request.POST.get('city')
        get_degree = request.POST.get('degree')
        get_profile_photo = request.FILES.get('profile_image')
        get_about_desc = request.POST.get('about_desc')
        get_role = request.POST.get('role')


        # Check if passwords match
        if get_password != get_confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/auth/signup/')

        # Check if email is already taken
        if CustomUser.objects.filter(email=get_email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('/auth/signup/')

        # Create a new user
        myuser = CustomUser.objects.create_user(
            username=get_email, 
            email=get_email, 
            password=get_password, 
            dob=get_dob, 
            phonenumber=get_phonenumber,
            city=get_city,
            degree=get_degree,
            first_name=get_first_name,
            last_name=get_last_name,
            profile_photo=get_profile_photo,
            about_desc=get_about_desc,
            role = get_role
        )

        # Save the user
        print(type(get_profile_photo))
        print(get_profile_photo)
        myuser.profile_photo = get_profile_photo
        myuser.save()

        # Authenticate and login the user
        user = authenticate(username=get_email, password=get_password)
        if user is not None:
            messages.success(request, 'User created successfully')
            return render(request, 'login.html')

    return render(request, 'signup.html')


def handleLogin(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        myuser= authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'logout success')
    return render(request,'login.html')