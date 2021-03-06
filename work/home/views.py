from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import FilesUpload
import requests
#from.forms import OrderForm, CreateUserForm

# Create your views here.


def index(request):

    return render(request, 'index.html')
    # return HttpResponse("this is my home")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is my about page")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


# def logout_request(request):
#   logout(request)
#   return render(request, 'index.html')


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def home(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document1 = FilesUpload.object.create(file=file2)
        document1.save()
        return HttpResponse("File uploaded")
    return render(request, "index.html")
