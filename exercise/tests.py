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
        self.assertContains(response, "Welcome to Exercise Gamification!", status_code=200) 
    def test_register_page(self):
        response = self.client.get('/accounts/signup/', follow=True)
        self.assertContains(response, "Sign Up", status_code=200) 
    def test_sign_in_page(self):
        response = self.client.get('/accounts/login/', follow=True)
        self.assertContains(response, "Sign In", status_code=200) 
    def test_sign_up_page(self):
        response = self.client.get('/register/', follow=True)
        self.assertContains(response, "REGISTER FOR EXERCISE GAMIFICATION", status_code=200) 
    def test_password_reset_page(self):
        response = self.client.get('/accounts/password/reset/', follow=True)
        self.assertContains(response, "Password Reset", status_code=200) 
    def test_user_home_page(self):
        response = self.client.get('/profile/', follow=True)
        self.assertContains(response, "Sign In", status_code=200) 
    def test_log_workout_page(self):
        response = self.client.get('/LogNW/', follow=True)
        self.assertContains(response, "Sign In", status_code=200) 
    def test_my_workouts_page(self):
        response = self.client.get('/LogNW/', follow=True)
        self.assertContains(response, "Sign In", status_code=200) 
    def test_my_badges_page(self):
        response = self.client.get('/badges/', follow=True)
        self.assertContains(response, "Sign In", status_code=200) 
    def test_current_weather_page(self):
        response = self.client.get('/weather/', follow=True)
        self.assertContains(response, "What's the weather like?", status_code=200)     
    def test_log_out_page(self):
        response = self.client.get('/logout/', follow=True)
        self.assertContains(response, "You have been logged out", status_code=200)     


