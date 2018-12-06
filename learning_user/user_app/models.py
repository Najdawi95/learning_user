# import ....

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # Creat relationship (dont inherit form user)
    user = models.OneToOneField(User)

    # Add any addditional attributes you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # built-in attr of django.contrib.auth.models.User !
        return self.user.username
