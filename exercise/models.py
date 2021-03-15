from django.db import models

# Create your models here.


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

    exercise_type = models.CharField(max_length=3, choices=EXERCISE_CHOICES, default='CAR', null=True)
    exercise_date = models.DateTimeField('date completed', null=True)
    time_taken = models.IntegerField(default=0, null=True)
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='daily workout', null=True)


