from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from .forms import ExerciseForm, PostForm
from .models import Exercise, Profile, City, Post
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, CityForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, RedirectView
import requests
from django.core.exceptions import PermissionDenied
from django_oso.auth import authorize


# Utilized tutorial found at https://www.youtube.com/watch?v=FdVuKt_iuSI to create user profiles model/to register
# users in the app database

# Source for navigation bar and base template
# https://www.selimatmaca.com/211-base-template/

def directions(request):
    return render(request, 'exercise/directions.html')

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        return HttpResponseRedirect(reverse('exercise:posts'))
    elif request.method == 'GET':
        form = PostForm()
        context = {'form': form}
        return render(request, 'exercise/new_post.html', context)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created_at')[:10]
    authorized_posts = []
    for post in posts:
        try:
            authorize(request, post, action="view")
            authorized_posts.append(post)
        except PermissionDenied:
            continue
    return render(request, 'exercise/posts.html', {'posts': authorized_posts})


@login_required
def profile(request):
    exercise = Exercise.objects.filter(profile=request.user.profile)
    total_points = exercise.aggregate(total_points=Sum('points'))

    # SAVING POINTS TO PROFILE OF USER
    model = Profile
    if list(total_points.values())[0] is None:
        model.workout_points = 0
    else:
        model.workout_points = list(total_points.values())[0]
    request.user.profile.save()
    points = model.workout_points

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():  # and p_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated! You are now able to log in')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
        'total_points': total_points,
        'points': points
    }
    return render(request, 'exercise/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated! You are now able to log in')
            return HttpResponseRedirect(reverse('exercise:profile'))
        else:
            print("Something went wrong, please try again.")
        note = "Something went wrong, please try again."
        new_form = UserUpdateForm()
        return render(request, 'exercise/editprofile.html', {'profileform':new_form, 'note':note})
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'exercise/editprofile.html', {'u_form': u_form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            note = 'Your account has been created! You are now able to log in'
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'exercise/register.html', {'form': form})


def badges(request):
    exercise = Exercise.objects.filter(profile=request.user.profile)
    total_points = exercise.aggregate(total_points=Sum('points'))
    date = Exercise.objects.filter()
    context = {'total_points': total_points}
    return render(request, 'exercise/badges.html', context)


def the_weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e1d3b12bb66e2fbb73a45268f086a35e'
    weather_data = []
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    # request the API data and convert the JSON to Python data types
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'exercise/weather.html', context)


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e1d3b12bb66e2fbb73a45268f086a35e'
    weather_data = []
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    # request the API data and convert the JSON to Python data types
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'exercise/index.html', context)


def home(request):
    return render(request, 'exercise/HomeLogin.html')


@login_required
def my_ws(request):
    form = ExerciseForm()
    exercise = Exercise.objects.filter(profile=request.user.profile)
    total_points = exercise.aggregate(total_points=Sum('points'))
    Profile.workout_points = total_points
    args = {'form': form, 'exercise': exercise, 'total_points': total_points}
    return render(request, 'exercise/MyWorkouts.html', args)


@login_required
def log_nws(request):
    if request.method == 'POST':
        filled_form = ExerciseForm(request.POST)
        print(filled_form.errors)
        total = 0
        # model.points = 5
        # user_profile = Profile._meta.get_field('workout_points')
        if filled_form.is_valid():
            model = filled_form.save(commit=False)
            model.points = 5
            model.profile = Profile.objects.get(user=request.user)

            # model.exercise = Exercise.objects.get(exercise_type=request.user)
            if filled_form.cleaned_data['time_taken'] == 'Longer Workout (Between 30-59 min)':
                model.points*=2
            elif filled_form.cleaned_data['time_taken'] == 'Long Workout (Between 60 and 119 min)':
                model.points*=4
            elif filled_form.cleaned_data['time_taken'] == 'Very Long Workout (120 min or greater)':
                model.points*=8
            if filled_form.cleaned_data['exercise_type'] == 'Cardio':
                model.points*=2
            elif filled_form.cleaned_data['exercise_type'] == 'Strength':
                model.points*=3
            elif filled_form.cleaned_data['exercise_type'] == 'Sports':
                model.points*=4
            if filled_form.cleaned_data['location'] == 'Outdoors':
                model.points*=2

            # request.user.profile.workout_points += model.points
            request.user.profile.award_points(model.points)
            request.user.profile.save()
            model.save()
            return HttpResponseRedirect(reverse('exercise:my_ws'))
        else:
            print("Something went wrong, please try again.")
        note = "Something went wrong, please try again."
        new_form = ExerciseForm()
        return render(request, 'exercise/LogNW.html', {'exerciseform':new_form, 'note':note})
    else:
        form = ExerciseForm()
        return render(request, 'exercise/LogNW.html', {'exerciseform': form})


@login_required
def leaderboard(request):
    all_users = User.objects.all()
    leader_board = Profile.objects.order_by('-workout_points')[:]
    context = {
        'all_users': all_users,
        'leader_board': leader_board
    }
    return render(request, 'exercise/leaderboard.html', context)


