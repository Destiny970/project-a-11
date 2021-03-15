from django import forms 
from .models import Exercise

class ExerciseForm(forms.ModelForm): 

    exercise_type = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=Exercise.EXERCISE_CHOICES,
    )
    
    ## the following stack overflow post aided in writing the code for this widget
    ## https://stackoverflow.com/questions/49440853/django-2-0-modelform-datefield-not-displaying-as-a-widget 
    exercise_date = forms.DateTimeField(widget=forms.DateInput(
        format=('%m/%d/%Y'), 
        attrs={
            'class':'form-control', 
            'placeholder':'Select a date', 
            'type':'date'
            }
    ))

    time_taken = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control', 
            'placeholder':'Workout duration'#, 
            # 'type':'time'
            }
    ))

    # points = forms.IntegerField(widget=forms.errors())

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'size': 100,
            'placeholder': 'Provide thoughts on your workout here.'
        }
    ))

    class Meta:
        model = Exercise
        ## fields =  ['exercise_type', 'exercise_date', 'time_taken', 'points', 'description']
        fields = ['exercise_date', 'time_taken', 'description']
        labels = {
            'exercise_type': 'exercise_type_descript',
            'exercise_date': 'exercise_date_descript',
            # 'points': 'points_descript',
            'time_taken': 'time_taken_descript',
            'description': 'Provide thoughts on your workout',
            }
