from .models import *
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Authentication Views
def index_view(request):
    return render(request, "app/index.html")


def register_view(request):
    return render(request, "app/register.html")


def register_submit(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
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

        if not email:
            messages.error(request, "The 'Email' field can not be empty!")
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
            user = Customer.objects.create_user(username, email, password)
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


# def login_submit(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
        
#         if not username:
#             messages.error(request, "The 'Username' field can not be empty!")
#             return render(request, "app/index.html")
#         if not password:
#             messages.error(request, "The 'Password' field can not be empty!")
#             return render(request, "app/index.html")

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, "You have logged in successfully!")
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             messages.error(request, "Invalid username and/or password.")
#             return render(request, "app/index.html")
#     else:
#         return render(request, "app/index.html")

def login_submit(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        try:
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "You have logged in successfully!")
            return HttpResponseRedirect(reverse("index"))
        except:
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
    try:
        user = Customer.objects.get(username=username)
    except Customer.DoesNotExist:
        user = None

    total_calories = Food.objects.filter(customer=user).aggregate(Sum('calories'))['calories__sum'] or Decimal('0.00')
    total_fat = Food.objects.filter(customer=user).aggregate(Sum('fat'))['fat__sum'] or Decimal('0.00')
    total_protein = Food.objects.filter(customer=user).aggregate(Sum('protein'))['protein__sum'] or Decimal('0.00')
    total_carbs = Food.objects.filter(customer=user).aggregate(Sum('carbs'))['carbs__sum'] or Decimal('0.00')

    context = {
        "user": user,
        "total_calories": str(round(total_calories, 2)),
        "total_fat": str(round(total_fat, 2)),
        "total_protein": str(round(total_protein, 2)),
        "total_carbs": str(round(total_carbs, 2)),
    }

    return render(request, "app/profile.html", context)


def profile_settings_view(request, username):
    try:
        user = Customer.objects.get(username=username)
    except Customer.DoesNotExist:
        user = None

    context = {
        "join_date": user.date_joined.date(),
        "user": user,
    }

    return render(request, "app/settings.html", context)


def profile_edit_submit(request, username):
    if request.method == "POST":
        try:
            user = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            user = None

        # Profile Credentials
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Password Credentials
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        # Address Credentials
        city = request.POST["city"]
        state = request.POST["state"]
        country = request.POST["country"]

        # Social Platforms Credentials
        website = request.POST["website"]
        facebook = request.POST["facebook"]
        instagram = request.POST["instagram"]
        twitter = request.POST["twitter"]
        github = request.POST["github"]

        # Job & Numbers Credentials
        job = request.POST.get("job", "Null")
        phone_number = request.POST.get("phone_number", "Null")
        mobile_phone = request.POST.get("mobile_phone", "Null")

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        if current_password and new_password and confirm_password:
            if user.check_password(current_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                else:
                    return messages.error(request, "Passwords should match!")
            else:
                return messages.error(request, "That's not your password!")
        
        user.city = city
        user.state = state
        user.country = country

        user.website = website
        user.facebook = facebook
        user.instagram = instagram
        user.twitter = twitter
        user.github = github
        user.job = job
        user.phone_number = phone_number
        user.mobile_number = mobile_phone

        user.save()

        messages.success(request, "Changes saved successfully!")
        return HttpResponseRedirect(reverse("index"))
    else:
        messages.error(request, "An error occured!")
        return HttpResponseRedirect(reverse("index"))


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
