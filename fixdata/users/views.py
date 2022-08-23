'''Modules for proper functoning of this view.py'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create a view for the index page.
def index(request):
    '''a function for index page display'''
    return render(request, "index.html")

# Create a view function for handling signup and creating new users.
def signup(request):
    '''a function for signup page display'''
    return render(request, "signup.html")

def adduser(request):
    '''a function for handling user creation'''

    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(username=email):
            messages.error(request, "Email already exist.")
            return redirect('signup')

        if password != password1:
            messages.error(request, "Password does not match.")
            return redirect('signup')

        new_user = User.objects.create_user(
            username=email, email=email, password=password, first_name=fullname
            )

        new_user.save()

        messages.success(request, "Your Account has been successfully created.")
        return redirect('signin')

# Create a view function for handling logging in.
def signin(request):
    '''a function for index page display'''
    return render(request, "signin.html")

def login_user(request):
    '''a function for handling login'''
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fullname = user.first_name
            email = user.email
            return redirect('dashboard', {'fullname' : fullname, 'email' : email})

        messages.error(request, "Bad Credentials")
        return redirect('signin')

    return render(request, "signin.html")
