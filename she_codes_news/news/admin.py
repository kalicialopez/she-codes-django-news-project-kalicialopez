from django.contrib import admin
from . import models
from .models import NewsStory

# Register your models here.

admin.site.register(models.NewsStory)

admin.site.register(models.Comment)