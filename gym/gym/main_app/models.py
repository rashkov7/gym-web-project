from django.db import models


class GymInfoModel(models.Model):
    h1 = models.CharField(max_length=200)
    h1_span = models.CharField(max_length=20, null=False, blank=True)
    quote = models.CharField(max_length=250, null=False, blank=True)
    facebook_URL = models.URLField(null=False, blank=True)
    tweeter_URL = models.URLField(null=False, blank=True)
    instagram_URL = models.URLField(null=False, blank=True)
    working_time = models.TextField(null=False, blank=True)


