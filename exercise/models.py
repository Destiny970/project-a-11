from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    workout_points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def total_points(self):
    #     return self.workout_points + 100

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


class Exercise(models.Model):
    def __str__(self):
        return self.description

    """
    This method sets the points given a time taken (should probably modify later)
    """
    def set_points(self):
        self.points = int(self.time_taken) * 10

    EXERCISE_CHOICES = [
        ('CAR', 'cardio'),
        ('STR', 'strength'),
        ('SPT', 'sports'),
        ('FLX', 'yoga/flexibility'),
    ]
    TIME_CHOICES = [
        ('LESS_THAN_30', 'Quick Workout (Between 1-29 min)'),
        ('LESS_THAN_1_HR', 'Longer Workout (Between 30-59 min'),
        ('BETWEEN_1_AND_2_HRS', 'Long Workout (Between 60 and 119 min'),
        ('MORE_THAN_2_HRS', 'Very Long Workout (120 min or greater)'),
    ]
    exercise_type = models.CharField(max_length=3, choices=EXERCISE_CHOICES, default='CAR')
    exercise_date = models.DateTimeField('date completed', null=True)
    # time_taken = models.IntegerField(default=0)
    time_taken = models.CharField(max_length=20, choices=TIME_CHOICES, default='LESS_THAN_30')
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=200, blank=True)
    profile = models.ForeignKey('Profile', null=True, on_delete=models.CASCADE)


