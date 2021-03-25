from django import forms 
from .models import Exercise, Profile
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']


class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        exclude = ['points', 'profile']
        widgets = {
            ## the following stack overflow post aided in writing the code for the exercise_date widget
            ## https://stackoverflow.com/questions/49440853/django-2-0-modelform-datefield-not-displaying-as-a-widget
            'exercise_date': forms.DateTimeInput(format=('%m/%d/%Y'),attrs={'class':'form-control','type':'date'}),
            'description': forms.TextInput(attrs={'class':'form-control','size': 50,'placeholder': 'Provide thoughts on your workout here.'}),
        }

