from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from .forms import ExerciseForm
from .models import Exercise

def index(request):
    return render(request, 'exercise/index.html')
#
def home(request):
    return render(request, 'exercise/HomeLogin.html')


def user_home(request):
    return render(request, 'exercise/UserHome.html')


def log_nws(request):
    if request.method == 'POST':
        filled_form = ExerciseForm(request.POST)
        print(filled_form.errors)
        if filled_form.is_valid():
            filled_form.save()
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