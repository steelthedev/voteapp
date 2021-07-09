
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from random import randint

# Create your views here.

def RegistrationView(request):
    return render(request,'app/registerationview.html')

def register(request):
    if request.method == "POST":

        username = request.POST.get("username")
        mat_no = request.POST.get("mat_no").upper()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2" )
        db_query = UserVote.objects.filter(mat_no=mat_no)
        if len(username) < 4:

            messages.info(request, 'username must be more than four characters')
            return redirect('app:home')

        elif password1 != password2:
            messages.info(request, 'Passwords does not match')
            return redirect('app:home')
        elif "LSC" not in mat_no:
            messages.info(request, 'you are not a life science member')
            return redirect('app:home')
        elif db_query:
            messages.info(request, 'This Matriculation Number Belongs TO Another User')
            return redirect('app:home')
        else:
            password = make_password(password1)
            user = User.objects.create(username = username , password = password)
            user.refresh_from_db()
            user_vote= UserVote.objects.get(user=user)
            user_vote.mat_no= mat_no
            random_number= randint(0,289)
            user_vote_id = f"LSV-{random_number}"
            user_vote.voters_id = user_vote_id
            user_vote.save()


            messages.info(request, f" your profile has been created succesfully, proceed to login")

            return redirect('app:home')
def loginview(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password")

        user_filter = User.objects.filter(username=username)

        if user_filter:
           

            user = authenticate(request,username = username , password = password1)
            

            if user is not None:

                login(request, user)
                return redirect('app:user_view')
            else:
                messages.info(request, "Password Incorrect")
                return redirect("app:login")

        else:
            messages.info(request, " Username does not exist ")
            return redirect('app:login')
    return render(request, 'app/login.html')

def user_view(request):
    if request.user.is_authenticated:

        user_details = UserVote.objects.get(user=request.user)
        candidate = Candidates.objects.all()
        context ={
            'user':user_details,
            'candidates':candidate
        }

    return render(request ,'app/user.html' , context)

def vote(request, id):
    if request.user.is_authenticated:
        candidate = Candidates.objects.get(pk=id)
        
        candidate.is_count=True

        candidate.count += 1

        candidate.save()

        

        messages.info(request, 'vote casted succesfully')
        return redirect('app:user_view')

