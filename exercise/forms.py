from django import forms 
from .models import Exercise, Profile, City, Post
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['contents', 'access_level']
        widgets = {
            # 'contents': forms.TextInput(attrs={'class':'form-control','size': 1000,'placeholder': 'Write your tip/trick here.'}),
            'contents': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': 'Write your tip/trick/accomplishment here.'}),
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']


class ExerciseForm(forms.ModelForm):

    class Meta:
        LOCATION_CHOICES = [
            ('Indoors', 'Indoors'),
            ('Outdoors', 'Outdoors')
        ]
        model = Exercise
        exclude = ['points', 'profile']
        location = forms.ChoiceField(choices=LOCATION_CHOICES)
        widgets = {
            ## the following stack overflow post aided in writing the code for the exercise_date widget
            ## https://stackoverflow.com/questions/49440853/django-2-0-modelform-datefield-not-displaying-as-a-widget
            'exercise_date': forms.DateTimeInput(format=('%m/%d/%Y'),attrs={'class':'form-control','type':'date'}),
            # 'description': forms.TextInput(attrs={'class':'form-control','size': 50,'placeholder': 'Provide thoughts on your workout here.'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5, 'placeholder': 'Provide thoughts on your workout here.'}),
        }



