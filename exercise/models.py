from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

# Source for 3rd party weather API
# https://www.digitalocean.com/community/tutorials/how-to-build-a-weather-app-in-django


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class InstagramAccount(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Publication(models.Model):
    picture = models.ImageField(upload_to="profile_pics")
    publish_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    instagram_account_id = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe("<img src='/%s' max-width='50' />" % self.picture)

    image_tag.short_description = "Picture"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # badges = models.ImageField(default='default.jpg', upload_to='profile_pics')
    workout_points = models.IntegerField(default=0)
    # interface = models.ForeignKey(GamificationInterface, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def award_points(self, workout_points):
        self.workout_points += workout_points
        self.save()


class Exercise(models.Model):
    def __str__(self):
        return self.description

    """
    This method sets the points given a time taken (should probably modify later)
    """
    def set_points(self):
        ## self.points = int(self.time_taken) * 10
        if (self.time_taken == 'LESS_THAN_30'):
            self.points = 5
        elif (self.time_taken == 'LESS_THAN_1_HR'):
            self.points = 10
        elif (self.time_taken == 'BETWEEN_1_AND_2_HRS'):
            self.points = 15 
        else:
            self.points = 20 

    EXERCISE_CHOICES = [
        ('CAR', 'Cardio'),
        ('STR', 'Strength'),
        ('SPT', 'Sports'),
        ('FLX', 'Yoga/Flexibility'),
    ]
    TIME_CHOICES = [
        ('LESS_THAN_30', 'Quick Workout (Between 1-29 min)'),
        ('LESS_THAN_1_HR', 'Longer Workout (Between 30-59 min)'),
        ('BETWEEN_1_AND_2_HRS', 'Long Workout (Between 60 and 119 min)'),
        ('MORE_THAN_2_HRS', 'Very Long Workout (120 min or greater)'),
    ]
    LOCATION_CHOICES = [
        ('INSIDE', 'Indoors'),
        ('OUTSIDE', 'Outdoors')
    ]
    exercise_type = models.CharField(max_length=3, choices=EXERCISE_CHOICES, default='CAR')
    location = models.CharField(max_length=7, choices=LOCATION_CHOICES, default='INSIDE')
    exercise_date = models.DateTimeField('date completed', null=True)
    # time_taken = models.IntegerField(default=0)
    time_taken = models.CharField(max_length=20, choices=TIME_CHOICES, default='LESS_THAN_30')
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=200, blank=True)
    profile = models.ForeignKey('Profile', null=True, on_delete=models.CASCADE)

    # total_points = models.IntegerField(default=0)


# from pinax.badges.base import Badge, BadgeAwarded
# from pinax.badges.registry import badges
# from django_gamification.models import GamificationInterface, UnlockableDefinition, BadgeDefinition, Category

# UnlockableDefinition.objects.create(
#     name='Bronze',
#     description='You just reached the bronze level!',
#     points_required=500
# )
#
# BadgeDefinition.objects.create(
#     name='Bronze Badge',
#     description='You just earned the bronze badge!',
#     points=500,
#     category=Category.objects.create(name='Bronze Badge', description='This is level 1 of the badges')
# )


# class BadgeAward(Badge):
#     slug = 'points'
#     levels = [
#         "Bronze",
#         "Silver",
#         "Gold",
#     ]
#     events = [
#         "points_awarded"
#     ]
#     multiple = False
#
#     def award(self, **state):
#         user = state["user"]
#         workout_points = user.profile.workout_points
#         if workout_points > 1000:
#             return BadgeAwarded(level=3)
#         elif workout_points > 750:
#             return BadgeAwarded(level=2)
#         elif workout_points > 500:
#             return BadgeAwarded(level=1)
#
#
# badges.register(BadgeAward)
