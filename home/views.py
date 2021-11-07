from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def homepage_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('/')

    return render(request, 'login.html', {})