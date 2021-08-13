from .models import *
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Authentication Views
def back(request):
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def index_view(request):
    return render(request, "app/index.html")


def register_view(request):
    return render(request, "app/register.html")


def register_submit(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        has_atleast_eight_characters = False
        has_atleast_one_digit = any(map(str.isdigit, password))
        has_atleast_one_upper = any(map(str.isupper, password))
        has_atleast_one_lower = any(map(str.islower, password))
        has_no_forbidden = False

        if len(str(password)) >= 8:
            has_atleast_eight_characters = True

        if not str(password).__contains__('!') or not str(password).__contains__('$') or not str(password).__contains__('#') or not str(password).__contains__('%'):
            has_no_forbidden = True

        if not username:
            messages.error(request, "The 'Username' field can not be empty!")
            return render(request, "app/index.html")

        if not password:
            messages.error(request, "The 'Password' field can not be empty!")
            return render(request, "app/index.html")

        if not confirmation:
            messages.error(request, "The 'Confirm password' field can not be empty!")
            return render(request, "app/index.html")

        if password != confirmation:
            messages.error(request, "Passwords must match!")
            return render(request, "app/index.html")

        if not has_atleast_eight_characters:
            messages.error(request, "The password can not contain less than 8 characters!")
            return render(request, "app/index.html", )

        if not has_atleast_one_digit:
            messages.error(request, "The password should contains atleast one digit!")
            return render(request, "app/index.html")

        if not has_atleast_one_upper:
            messages.error(request, "The password should contains atleast one upper character!")
            return render(request, "app/index.html")

        if not has_atleast_one_lower:
            messages.error(request, "The password should contains atleast one lower character!")
            return render(request, "app/index.html")

        if not has_no_forbidden:
            messages.error(request, "The password should not contains '!', '$', '#' or '%'!")
            return render(request, "app/index.html")

        try:
            user = Customer.objects.create_user(username, password)
            user.save()
            login(request, user)
            messages.success(request, "You have registered successfully!")
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            messages.error(request, "Username already taken.")
            return render(request, "app/index.html")
    else:
        return render(request, "app/index.html")


def login_view(request):
    return render(request, "app/login.html")


def login_submit(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        if not username:
            messages.error(request, "The 'Username' field can not be empty!")
            return render(request, "app/index.html")
        if not password:
            messages.error(request, "The 'Password' field can not be empty!")
            return render(request, "app/index.html")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid username and/or password.")
            return render(request, "app/index.html")
    else:
        return render(request, "app/index.html")


def logout_view(request):
    return render(request, "app/logout.html")


def logout_submit(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return HttpResponseRedirect(reverse("index"))


# Profile Views
def profile_view(request, username):
    user = Customer.objects.get(username=username)

    context = {
        "user": user
    }

    return render(request, "app/profile.html", context)


def profile_settings_view(request, username):
    user = Customer.objects.get(username=username)

    context = {
        "join_date": user.date_joined.date(),
        "user": user
    }

    return render(request, "app/settings.html", context)


def profile_edit_submit(request, username):
    pass


def profile_delete_view(request, username):
    pass


def profile_delete_submit(request, username):
    pass


# Workouts Views
def workouts(request):
    pass


def workout(request, id):
    pass


def workout_create(request):
    pass


def workout_create_submit(request):
    pass


def workout_edit(request, id):
    pass


def workout_edit_submit(request, id):
    pass


def workout_delete(request, id):
    pass


def workout_delete_submit(request, id):
    pass


# Tasks Views
def tasks(request):
    pass


def task(request, id):
    pass


def task_create(request):
    pass


def task_create_submit(request):
    pass


def task_edit(request, id):
    pass


def task_edit_submit(request, id):
    pass


def task_delete(request, id):
    pass


def task_delete_submit(request, id):
    pass



# BMIs Views
def bmis(request):
    pass


def bmi(request, id):
    pass


def bmi_create(request):
    pass


def bmi_create_submit(request):
    pass


def bmi_edit(request, id):
    pass


def bmi_edit_submit(request, id):
    pass


def bmi_delete(request, id):
    pass


def bmi_delete_submit(request, id):
    pass


# Calorie Counters Views
def calorie_counters(request):
    pass


def calorie_counter(request, id):
    pass


def calorie_counter_create(request):
    pass


def calorie_counter_create_submit(request):
    pass


def calorie_counter_edit(request, id):
    pass


def calorie_counter_edit_submit(request, id):
    pass


def calorie_counter_delete(request, id):
    pass


def calorie_counter_delete_submit(request, id):
    pass
