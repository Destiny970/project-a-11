from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Exercise, Profile
import unittest

class ExerciseModelSetPointMethodTests(TestCase):
    def test_default(self):
        ex_obj = Exercise()
        ex_obj.set_points()
        self.assertEqual(ex_obj.points, 20)
    def test_second_branch(self):
        ex_obj = Exercise(time_taken='LESS_THAN_1_HR')
        ex_obj.set_points()
        self.assertEqual(ex_obj.points, 10)
    def test_third_branch(self):
        ex_obj = Exercise(time_taken='BETWEEN_1_AND_2_HRS')
        ex_obj.set_points()
        self.assertEqual(ex_obj.points, 15)
    def test_else_branch(self):
        ex_obj = Exercise(time_taken='MORE_THAN_2_HRS')
        ex_obj.set_points()
        self.assertEqual(ex_obj.points, 20)

## The following Django documentation, accessible through the below url, was used to help write the code in this test class.
## https://docs.djangoproject.com/en/3.1/topics/testing/tools/
## Test class ensures that all URL paths are correctly functioning when the a user is not logged in. 
class WorkingURLPathsNotLoggedIn(TestCase):
    def test_home_page(self):
        response = self.client.get('/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_admin_page(self):
        response = self.client.get('/admin/', follow=True)
        self.assertContains(response, "Username:", status_code=200) 
    def test_profile_page(self):
        response = self.client.get('/profile/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_login_page(self):
        response = self.client.get('/login/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_logout_page(self):
        response = self.client.get('/logout/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_logNW_page(self):
        response = self.client.get('/LogNW/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_my_workouts_page(self):
        response = self.client.get('/MyWorkouts/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
#     def test_weather_page(self):
#         response = self.client.get('/weather/', follow=True)
#         self.assertContains(response, "Login with Google", status_code=200) 
    def test_edit_profile_page(self):
        response = self.client.get('/editprofile/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_badges_page(self):
        response = self.client.get('/badges/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_posts_page(self):
        response = self.client.get('/posts/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_newpost_page(self):
        response = self.client.get('/newpost/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_directions_page(self):
        response = self.client.get('/directions/', follow=True)
        self.assertContains(response, "HOW TO USE THE APP", status_code=200) 
    def test_leaderboard_page(self):
        response = self.client.get('/leaderboard/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_edit_location_page(self):
        response = self.client.get('/editlocation/', follow=True)
        self.assertContains(response, "Login with Google", status_code=200) 
    def test_not_logged_directions_page(self):
        response = self.client.get('/notloggeddirections/', follow=True)
        self.assertContains(response, "HOW TO USE THE APP", status_code=200) 
