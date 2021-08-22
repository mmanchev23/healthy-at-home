from .models import *
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Authentication Views
def index(request):
    return render(request, "app/index.html")

def sign_up(request):
    return render(request, "app/sign_up.html")

def sign_up_submit(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

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
            return render(request, "app/sign_up.html")

        if not email:
            messages.error(request, "The 'Email' field can not be empty!")
            return render(request, "app/sign_up.html")

        if not password:
            messages.error(request, "The 'Password' field can not be empty!")
            return render(request, "app/sign_up.html")

        if not confirm_password:
            messages.error(request, "The 'Confirm password' field can not be empty!")
            return render(request, "app/sign_up.html")

        if password != confirm_password:
            messages.error(request, "Passwords must match!")
            return render(request, "app/sign_up.html")

        if not has_atleast_eight_characters:
            messages.error(request, "The password can not contain less than 8 characters!")
            return render(request, "app/sign_up.html", )

        if not has_atleast_one_digit:
            messages.error(request, "The password should contains atleast one digit!")
            return render(request, "app/sign_up.html")

        if not has_atleast_one_upper:
            messages.error(request, "The password should contains atleast one upper character!")
            return render(request, "app/sign_up.html")

        if not has_atleast_one_lower:
            messages.error(request, "The password should contains atleast one lower character!")
            return render(request, "app/sign_up.html")

        if not has_no_forbidden:
            messages.error(request, "The password should not contains '!', '$', '#' or '%'!")
            return render(request, "app/sign_up.html")

        try:
            user = Customer.objects.create_user(username, email, password)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "You have registered successfully!")
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            messages.error(request, "Username already taken.")
            return render(request, "app/sign_up.html")
    else:
        return render(request, "app/sign_up.html")

def sign_in(request):
    return render(request, "app/sign_in.html")

def sign_in_submit(request):
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
            return render(request, "app/sign_in.html")
    else:
        return render(request, "app/sign_in.html")

def sign_out(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return HttpResponseRedirect(reverse("index"))

# Profile Views
def profile(request):
    try:
        user = Customer.objects.get(pk=request.user.pk)
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

def profile_edit(request):
    try:
        user = Customer.objects.get(pk=request.user.pk)
    except Customer.DoesNotExist:
        user = None

    context = {
        "join_date": user.date_joined.date(),
        "user": user,
    }

    return render(request, "app/profile_edit.html", context)

def profile_edit_submit(request):
    if request.method == "POST":
        try:
            user = Customer.objects.get(pk=request.user.pk)
        except Customer.DoesNotExist:
            user = None

        # Profile Credentials
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if "img" in request.FILES:
            profile_picture = request.FILES["img"]
        else:
            profile_picture = user.profile_picture

        # Password Credentials
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # Address Credentials
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")

        # Social Platforms Credentials
        website_link = request.POST.get("website_link")
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        twitter = request.POST.get("twitter")
        github = request.POST.get("github")

        # Job & Numbers Credentials
        job = request.POST.get("job")
        phone_number = request.POST.get("phone_number")
        mobile_number = request.POST.get("mobile_number")

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        
        user.profile_picture = profile_picture

        context = {
            "user": user,
        }

        if current_password:
            if new_password:
                if confirm_password:
                    if user.check_password(current_password):
                        if new_password == confirm_password:
                            user.set_password(new_password)
                            user.save()
                            messages.success(request, "Password updated successfully!")
                            return HttpResponseRedirect(reverse("profile", kwargs=context))
                        else:
                            messages.error(request, "Passwords should match!")
                            return HttpResponseRedirect(reverse("profile_edit", kwargs=context))
                    else:
                        messages.error(request, "That's not your current password!")
                        return HttpResponseRedirect(reverse("profile_edit", kwargs=context))
                else:
                    messages.error(request, "'Confirm Password' field can not be empty!")
                    return HttpResponseRedirect(reverse("profile_edit", kwargs=context))
            else:
                messages.error(request, "'New Password' field can not be empty!")
                return HttpResponseRedirect(reverse("profile_edit", kwargs=context))
        else:
            pass

        
        user.city = city
        user.state = state
        user.country = country

        user.website_link = website_link
        user.facebook = facebook
        user.instagram = instagram
        user.twitter = twitter
        user.github = github
        
        user.job = job
        user.phone_number = phone_number
        user.mobile_number = mobile_number

        user.save()

        messages.success(request, "Changes saved successfully!")
        return HttpResponseRedirect(reverse("index"))
    else:
        messages.error(request, "An error occured!")
        return HttpResponseRedirect(reverse("index"))

def profile_delete(request):
    return render(request, "app/profile_delete.html")

def profile_delete_submit(request):
    if request.method == "POST":
        try:
            user = Customer.objects.get(pk=request.user.pk)
        except Customer.DoesNotExist:
            user = None

        password = request.POST.get("password")

        context = {
            "user": user,
        }

        if user.check_password(password):
            user.delete()
            messages.success(request, "Profile deleted successfully!")
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Wrong password!")
            return HttpResponseRedirect(reverse("profile_edit", kwargs=context))
    else:
        messages.error(request, "An error occured!")
        return HttpResponseRedirect(reverse("profile_edit", kwargs=context))

# Tasks Views
def tasks(request):
    user = Customer.objects.get(pk=request.user.pk)
    tasks = Task.objects.filter(customer=user)

    context = {
        "user": user,
        "tasks": tasks,
    }

    return render(request, "app/tasks.html", context)

def task_create(request):
    if request.method == "POST":
        user = Customer.objects.get(pk=request.user.pk)
        title = request.POST.get("title")
        task = Task.objects.create(customer=user, title=title)
        messages.success(request, "Task created successfully!")
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "app/tasks.html")

def task_edit(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        title = request.POST.get("title")
        description = request.POST.get("description")
        completed = request.POST.get("completed")

        task.title = title
        task.description = description

        if completed == "on":
            task.completed = True
        else:
            task.completed = False

        task.save()

        messages.success(request, "Task updated successfully!")
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "app/tasks.html")

def task_delete(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "app/tasks.html")
