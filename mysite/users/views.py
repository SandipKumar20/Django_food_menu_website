from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.info(request, f"Welcome {username}, your account is created")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    #return render(request,"users/logout.html", {})
    return redirect("food:index")

@login_required
def profilepage(request):
    return render(request, "users/profile.html")

