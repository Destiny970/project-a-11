from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from .forms import ExerciseForm
from .models import Exercise

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def profile(request):
    return render(request, 'exercise/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            # return redirect('login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'exercise/register.html', {'form': form})


def index(request):
    return render(request, 'exercise/index.html')


def home(request):
    return render(request, 'exercise/HomeLogin.html')


def user_home(request):
    return render(request, 'exercise/UserHome.html')


def log_nws(request):
    if request.method == 'POST':
        filled_form = ExerciseForm(request.POST)
        print(filled_form.errors)
        total = 0
        if filled_form.is_valid():
            model = filled_form.save(commit=False)
            if filled_form.cleaned_data['time_taken'] == 'LESS_THAN_30':
                if filled_form.cleaned_data['exercise_type'] == 'CAR':
                    model.points += 10
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'STR':
                    model.points += 15
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'SPT':
                    model.points += 20
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'FLX':
                    model.points = 5
                    total += model.points
            elif filled_form.cleaned_data['time_taken'] == 'LESS_THAN_1_HR':
                if filled_form.cleaned_data['exercise_type'] == 'CAR':
                    model.points += 20
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'STR':
                    model.points += 30
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'SPT':
                    model.points += 40
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'FLX':
                    model.points += 10
                    total += model.points
            elif filled_form.cleaned_data['time_taken'] == 'BETWEEN_1_AND_2_HRS':
                if filled_form.cleaned_data['exercise_type'] == 'CAR':
                    model.points += 40
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'STR':
                    model.points += 60
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'SPT':
                    model.points += 80
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'FLX':
                    model.points = 20
                    total += model.points
            elif filled_form.cleaned_data['time_taken'] == 'MORE_THAN_2_HRS':
                if filled_form.cleaned_data['exercise_type'] == 'CAR':
                    model.points += 80
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'STR':
                    model.points += 120
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'SPT':
                    model.points += 160
                    total += model.points
                elif filled_form.cleaned_data['exercise_type'] == 'FLX':
                    model.points = 40
                    total += model.points
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


def my_ws(request):
    form = ExerciseForm()
    exercise = Exercise.objects.all()
    args = {'form': form, 'exercise': exercise}
    return render(request, 'exercise/MyWorkouts.html', args)


def my_points(request):
    # points = 0
    # form = ExerciseForm()
    # exercise = Exercise.objects.all()
    # total_points = 0
    # for wk in exercise:
    #     if wk.time_taken == 'LESS_THAN_30':
    #         wk.points += 10
    #         # wk.save()
    #     elif wk.time_taken == 'LESS_THAN_1_HR':
    #         wk.points += 20
    #         # wk.save()
    #     elif wk.time_taken == 'BETWEEN_1_AND_2_HRS':
    #         wk.points += 30
    #         # wk.save()
    #     else:
    #         wk.points += 40
    #         # wk.save()
    #     wk.total_time = wk.points
    # args = {'form': form, 'exercise': exercise}
    return render(request, 'exercise/MyPoints.html')




# Added 03/19/21
# from .models import Post
# from .forms import PostForm
#
#
# def list_posts(request):
#     posts = Post.objects.all().order_by('-created_at')[:10]
#     # posts_text = ""
#     # for post in posts:
#     #     posts_text += f"@{post.created_by} {post.contents}"
#     return render(request, 'exercise/list.html', {'posts': posts})
#
#
# def new_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         post = form.save(commit=False)
#         post.created_by = request.user
#         post.save()
#         return HttpResponseRedirect(reverse('public_private'))
#     elif request.method == 'GET':
#         form = PostForm()
#         return render(request, 'exercise/new_post.html', {'form': form})
#     else:
#         return HttpResponseNotAllowed(['GET', 'POST'])
# End


# lst = []
# points = 0
# for wk in exercise:
#     if wk.time_taken > 0 & wk.time_taken <= 60:
#         points = wk.time_taken * 10
#         lst.append(points)
#     elif wk.time_taken > 60 & wk.time_taken < 120:
#         points = wk.time_taken * 20
#         lst.append(points)
#     elif wk.time_taken <= 20:
#         points = wk.time_taken
#         lst.append(points)
#     else:
#         points = wk.time_taken * 30
#         lst.append(points)
# for item in lst:
#     total_points += item