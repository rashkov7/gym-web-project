from datetime import datetime

from django.db import models

from gym.auth_app.models import GymUser


class ProfileModel(models.Model):
    choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show')
    ]
    DEFAULT_CHOICE = choices[2][0]

    length_choice = max(len(x[0]) for x in choices)

    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=choices, max_length=length_choice, default=DEFAULT_CHOICE)
    photo = models.ImageField(blank=True, null=True)

    user = models.OneToOneField(GymUser, on_delete=models.CASCADE, primary_key=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        if self.birth_date:
            return datetime.now() - self.birth_date
        return 'Dont show'