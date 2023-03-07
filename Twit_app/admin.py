from django.contrib import admin
from .models import User, Post
from django.contrib.auth import get_user_model


admin.site.register(User)
admin.site.register(Post)
