# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST["username"]
            password = request.POST["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("login")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "register.html", context)


@login_required
def about(request):
    return render(request, "about.html")

