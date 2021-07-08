from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def RegistrationView(request):
    return render(request,'app/registerationview.html')

def register(request):
    username = request.POST.get("username")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2" )

    user = User.objects.create(username = username , password = password1)

    user.save()

    messages.info(request, " your profile has been created succesfully")

    return redirect('app:home')

