from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from .forms import ExerciseForm
from .models import Exercise, Profile, City
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, CityForm
# from django_gamification.models import Badge
from django.views.generic import TemplateView, RedirectView
import requests
# from pinax.badges.registry import badges
# ProfileUpdateForm

# Utilized tutorial found at https://www.youtube.com/watch?v=FdVuKt_iuSI to create user profiles model/to register
# users in the app database

# Source for navigation bar and base template
# https://www.selimatmaca.com/211-base-template/


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
        # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid():  # and p_form.is_valid():
            u_form.save()
            # p_form.save()
            messages.success(request, f'Your account has been updated! You are now able to log in')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'total_points': total_points,
        'points': points
        # 'p_form': p_form
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
            # messages.success(request, f'Your account has been created! You are now able to log in')
            note = 'Your account has been created! You are now able to log in'
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'exercise/register.html', {'form': form})


def badges(request):
    exercise = Exercise.objects.filter(profile=request.user.profile)
    total_points = exercise.aggregate(total_points=Sum('points'))

    context = {'total_points': total_points}
    return render(request, 'exercise/MyBadges.html', context)


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


# def user_home(request):
#     return render(request, 'exercise/UserHome.html')


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
            if filled_form.cleaned_data['time_taken'] == 'LESS_THAN_1_HR':
                model.points*=2
            elif filled_form.cleaned_data['time_taken'] == 'BETWEEN_1_AND_2_HRS':
                model.points*=4
            elif filled_form.cleaned_data['time_taken'] == 'MORE_THAN_2_HRS':
                model.points*=8
            if filled_form.cleaned_data['exercise_type'] == 'CAR':
                model.points*=2
            elif filled_form.cleaned_data['exercise_type'] == 'STR':
                model.points*=3
            elif filled_form.cleaned_data['exercise_type'] == 'SPT':
                model.points*=4
            if filled_form.cleaned_data['location'] == 'OUTSIDE':
                model.points*=2

            # request.user.profile.workout_points += model.points
            request.user.profile.award_points(model.points)
            request.user.profile.save()
            # badges.possibly_award_badge('points_awarded', user=request.user)
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


# def my_ws(request):
#     form = ExerciseForm()
#     exercise = Exercise.objects.all()
#     args = {'form': form, 'exercise': exercise}
#     return render(request, 'exercise/MyWorkouts.html', args)


# class WorkoutListView(ListView):
#     model = Exercise
#     template = 'exercise/MyWorkouts.html'
#     context_object_name = 'exercise'
#
#
# class UserWorkoutListView(ListView):
#     model = Exercise
#     template_name = 'exercise/user_workouts.html'
#     context_object_name = 'exercise'
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Exercise.objects.filter(author=user)


# def my_points(request):
#     return render(request, 'exercise/MyPoints.html')
