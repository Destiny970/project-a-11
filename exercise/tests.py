from django.test import TestCase
from .models import Exercise, Profile
import unittest

class ExerciseModelSetPointMethodTests(TestCase):
    def test_default(self):
        ex_obj = Exercise()
        ex_obj.set_points()
        self.assertEqual(ex_obj.points, 5)
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
class WorkingURLPaths(TestCase):
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
