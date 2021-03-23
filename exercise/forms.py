from django import forms 
from .models import Exercise
import datetime


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ExerciseForm(forms.ModelForm): 

    class Meta:
        model = Exercise
        exclude = ['points']
        widgets = {
            ## the following stack overflow post aided in writing the code for the exercise_date widget
            ## https://stackoverflow.com/questions/49440853/django-2-0-modelform-datefield-not-displaying-as-a-widget
            'exercise_date': forms.DateTimeInput(format=('%m/%d/%Y'),attrs={'class':'form-control','type':'date'}),
            'description': forms.TextInput(attrs={'class':'form-control','size': 50,'placeholder': 'Provide thoughts on your workout here.'}),
        }


# Added 03/19/21
# from django.forms import ModelForm
# from .models import Post
#
#
# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['contents', 'access_level']
# End