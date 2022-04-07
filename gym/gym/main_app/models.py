from django.contrib.auth import get_user_model
from django.db import models

from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


class GymInfoModel(models.Model):
    h1 = models.CharField(max_length=200)
    h1_span = models.CharField(max_length=20, null=False, blank=True)
    quote = models.CharField(max_length=250, null=False, blank=True)
    facebook_URL = models.URLField(null=False, blank=True)
    tweeter_URL = models.URLField(null=False, blank=True)
    instagram_URL = models.URLField(null=False, blank=True)
    working_time = models.TextField(null=False, blank=True)


class StarCoach(models.Model):
    owner = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='star_owner')
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='star_sender')
