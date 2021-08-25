import os
from .models import *
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
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

@login_required(redirect_field_name="sign_in/")
def sign_out(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return HttpResponseRedirect(reverse("index"))

@login_required(redirect_field_name="sign_in/")
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

@login_required(redirect_field_name="sign_in/")
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

@login_required(redirect_field_name="sign_in/")
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
        facebook = request.POST.get("facebook")
        instagram = request.POST.get("instagram")
        twitter = request.POST.get("twitter")

        # Job & Numbers Credentials
        job = request.POST.get("job")
        phone_number = request.POST.get("phone_number")

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

        user.facebook = facebook
        user.instagram = instagram
        user.twitter = twitter
        
        user.job = job
        user.phone_number = phone_number

        user.save()

        messages.success(request, "Changes saved successfully!")
        return HttpResponseRedirect(reverse("index"))
    else:
        messages.error(request, "An error occured!")
        return HttpResponseRedirect(reverse("index"))

@login_required(redirect_field_name="sign_in/")
def profile_delete(request):
    return render(request, "app/profile_delete.html")

@login_required(redirect_field_name="sign_in/")
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

@login_required(redirect_field_name="sign_in/")
def tasks(request):
    user = Customer.objects.get(pk=request.user.pk)
    tasks = Task.objects.filter(customer=user)

    context = {
        "user": user,
        "tasks": tasks,
    }

    return render(request, "app/tasks.html", context)

@login_required(redirect_field_name="sign_in/")
def task_create(request):
    if request.method == "POST":
        user = Customer.objects.get(pk=request.user.pk)
        title = request.POST.get("title")
        task = Task.objects.create(customer=user, title=title)
        messages.success(request, "Task created successfully!")
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "app/tasks.html")

@login_required(redirect_field_name="sign_in/")
def task_edit(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        if task.customer == request.user:
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
            messages.error(request, "No such rights!")
            return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "app/tasks.html")

@login_required(redirect_field_name="sign_in/")
def task_delete(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        if task.customer == request.user:
            task.delete()
            messages.success(request, "Task deleted successfully!")
            return HttpResponseRedirect(reverse("tasks"))
        else:
            messages.error(request, "No such rights!")
            return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "app/tasks.html")

@login_required(redirect_field_name="sign_in/")
def workouts(request):
    user = Customer.objects.get(pk=request.user.pk)
    workouts = Workout.objects.filter(Q(customer=user) | Q(public=True))

    context = {
        "user": user,
        "workouts": workouts,
    }

    return render(request, "app/workouts.html", context)

@login_required(redirect_field_name="sign_in/")
def workout_create(request):
    if request.method == "POST":
        user = Customer.objects.get(pk=request.user.pk)

        title = request.POST.get("title")

        if "workout_image" in request.FILES:
            workout_image = request.FILES["workout_image"]
        else:
            workout_image = os.path.basename("default_workout_image.png")
        
        video_url = request.POST.get("video_url")
        if video_url:
            video_url = request.POST.get("video_url")
        else:
            video_url = "https://www.youtube.com/embed/oAPCPjnU1wA"

        description = request.POST.get("description")
        if description:
            description = request.POST.get("description")
        else:
            description = "No description yet..."

        exercises = request.POST.get("exercises")
        if exercises:
            exercises = request.POST.get("exercises")
        else:
            exercises = "No exercises yet..."

        public = request.POST.get("public")
        if public == "on":
            public = True
        else:
            public = False
        
        workout = Workout.objects.create(
            customer=user,
            title=title,
            workout_image=workout_image,
            video_url=video_url,
            description=description,
            exercises=exercises,
            public=public,
        )
        
        messages.success(request, "Workout created successfully!")
        return HttpResponseRedirect(reverse("workouts"))
    else:
        return render(request, "app/workouts.html")

@login_required(redirect_field_name="sign_in/")
def workout(request, id):
    workout = Workout.objects.get(pk=id)

    context = {
        "workout": workout,
    }

    return render(request, "app/workout.html", context)

@login_required(redirect_field_name="sign_in/")
def workout_edit(request, id):
    if request.method == "POST":
        workout = Workout.objects.get(pk=id)
        if workout.customer == request.user:
            if "workout_image" in request.FILES:
                workout_image = request.FILES["workout_image"]
            else:
                workout_image = workout.workout_image

            title = request.POST.get("title")
            video_url = request.POST.get("video_url")
            description = request.POST.get("description")
            exercises = request.POST.get("exercises")
            public = request.POST.get("public")

            workout.title = title
            workout.workout_image = workout_image
            workout.video_url = video_url
            workout.exercises = exercises
            workout.description = description

            if public == "on":
                workout.public = True
            else:
                workout.public = False

            workout.save()

            messages.success(request, "Workout updated successfully!")
            return HttpResponseRedirect(reverse("workouts"))
        else:
            messages.error(request, "No such rights!")
            return HttpResponseRedirect(reverse("workouts"))
    else:
        return render(request, "app/workouts.html")

@login_required(redirect_field_name="sign_in/")
def workout_delete(request, id):
    if request.method == "POST":
        workout = Workout.objects.get(pk=id)
        if workout.customer == request.user:
            workout.delete()
            messages.success(request, "Workout deleted successfully!")
            return HttpResponseRedirect(reverse("workouts"))
        else:
            messages.error(request, "No such rights!")
            return HttpResponseRedirect(reverse("workouts"))
    else:
        return render(request, "app/workouts.html")

@login_required(redirect_field_name="sign_in/")
def meals_and_bmis(request):
    user = Customer.objects.get(pk=request.user.pk)
    bmis = BMICalculator.objects.filter(customer=user)
    meals = Food.objects.filter(customer=user)

    average_height = Decimal('0.00')
    average_weight = Decimal('0.00')
    average_result = Decimal('0.00')

    for bmi in bmis:
        average_height += bmi.height
        average_weight += bmi.weight
        average_result += bmi.result
    
    if len(bmis) > 0:
        average_height /= len(bmis)
        average_weight /= len(bmis)
        average_result /= len(bmis)
    else:
        average_height = Decimal('0.00')
        average_weight = Decimal('0.00')
        average_result = Decimal('0.00')

    total_calories = Food.objects.filter(customer=user).aggregate(Sum('calories'))['calories__sum'] or Decimal('0.00')
    total_fat = Food.objects.filter(customer=user).aggregate(Sum('fat'))['fat__sum'] or Decimal('0.00')
    total_protein = Food.objects.filter(customer=user).aggregate(Sum('protein'))['protein__sum'] or Decimal('0.00')
    total_carbs = Food.objects.filter(customer=user).aggregate(Sum('carbs'))['carbs__sum'] or Decimal('0.00')

    context = {
        "user": user,
        "bmis": bmis,
        "meals": meals,
        "average_height": average_height,
        "average_weight": average_weight,
        "average_result": average_result,
        "total_calories": str(round(total_calories, 2)),
        "total_fat": str(round(total_fat, 2)),
        "total_protein": str(round(total_protein, 2)),
        "total_carbs": str(round(total_carbs, 2)),
    }

    return render(request, "app/meals_and_bmis.html", context)

@login_required(redirect_field_name="sign_in/")
def meal_create(request):
    if request.method == "POST":
        user = Customer.objects.get(pk=request.user.pk)
        name = request.POST.get("name")
        calories = request.POST.get("calories")
        fat = request.POST.get("fat")
        carbs = request.POST.get("carbs")
        protein = request.POST.get("protein")
        meal = Food.objects.create(customer=user, name=name, calories=calories, fat=fat, carbs=carbs, protein=protein)
        messages.success(request, "Meal created successfully!")
        return HttpResponseRedirect(reverse("meals_and_bmis"))
    else:
        return render(request, "app/meals_and_bmis.html")
