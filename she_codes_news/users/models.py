from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    pass

    def __str__(self):
        return self.username

        def __str__(self):
            return "Profile of {}".format(self.user.username)
