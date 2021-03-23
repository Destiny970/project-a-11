from django.contrib import admin
from .models import Exercise, Profile

admin.site.register(Exercise)
admin.site.register(Profile)
# admin.site.register(User)

# Added 03/19/21
# from django.contrib.auth.admin import UserAdmin
# from.models import User, Post
# admin.site.register(User, UserAdmin)
# admin.site.register(Post)
# End
