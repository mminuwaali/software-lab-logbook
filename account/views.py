from . import forms
from django.contrib import auth, messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


def logout_view(request):
    auth.logout(request)
    return redirect("/")


def login_view(request):
    if request.method == "POST":
        user = auth.authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user:
            auth.login(request, user)
            return redirect("landing:index-view")

        messages.error(request, "Invalid credentials")
        return redirect("account:login-view")

    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get_or_create(name='student')[0])

            request.session['form_data'] = None
            return redirect("account:login-view")

        print(form.errors)
        request.session['form_data'] = form.data
        (messages.error(request, i) for i in form.errors.values())
        return redirect("account:register-view")
    
    return render(request, "account/register.html")