from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup_site(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        user_account = User.objects.create_user(username, email, password)
        user_account.save()
        return redirect('/')

    return render(request, 'sign_up.html', {})
