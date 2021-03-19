from django.db import models

# Added 03/19/21
# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     pass
#
#
# class Post(models.Model):
#     ACCESS_PUBLIC = 0
#     ACCESS_PRIVATE = 1
#     ACCESS_LEVEL_CHOICES = [
#         (ACCESS_PUBLIC, 'Public'),
#         (ACCESS_PRIVATE, 'Private')
#     ]
#     contents = models.CharField(max_length=140)
#     access_level = models.IntegerField(choices=ACCESS_LEVEL_CHOICES, default=ACCESS_PUBLIC)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# End


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

    exercise_type = models.CharField(max_length=3, choices=EXERCISE_CHOICES, default='CAR')
    exercise_date = models.DateTimeField('date completed', null=True)
    time_taken = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=200, blank=True)


