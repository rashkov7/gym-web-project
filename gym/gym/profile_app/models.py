from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from gym.auth_app.models import GymUser

from gym.helpers.validators import validator_name_only_alphabet_and_space, name_first_letter_validator

UserModel = get_user_model()


class ProfileModel(models.Model):
    MIN_CHARS = 3
    choices = [
        ('Do not show', 'Do not show'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    DEFAULT_CHOICE = choices[0][0]

    LENGTH_CHOICE = max(len(x[0]) for x in choices)

    first_name = models.CharField(
        max_length=30,
        verbose_name='First Name',
        validators=(
            name_first_letter_validator,
            validator_name_only_alphabet_and_space,
            MinLengthValidator(MIN_CHARS, f'Name must contains at least {MIN_CHARS} characters')
        ),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Last Name',
        validators=(
            validator_name_only_alphabet_and_space,
            MinLengthValidator(MIN_CHARS, f'Name must contains at least {MIN_CHARS} characters')
        ),
        blank=True,
        null=True,
    )
    birth_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(
        choices=choices,
        max_length=LENGTH_CHOICE,
        default=DEFAULT_CHOICE
    )
    photo = models.ImageField(blank=True, null=True, upload_to='images')

    crossfit_coach = models.BooleanField(default=False)
    yoga_coach = models.BooleanField(default=False)
    combat_coach = models.BooleanField(default=False)
    fitness_coach = models.BooleanField(default=False)
    dance_coach = models.BooleanField(default=False)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year
        return 'Unknown'

    def __str__(self):
        return self.full_name

    @property
    def is_stars_by_the_user(self):
        if self.star_owner.filter(owner__user=self.user):
            return True


class TestModel(models.Model):
    test = models.CharField(max_length=10)