from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from gym.helpers.validators import validator_name_only_alphabet_and_space

UserModel = get_user_model()


class WorkoutModel(models.Model):
    CROSSFIT = 'CROSSFIT'
    COMBAT = 'COMBAT'
    FITNESS = 'FITNESS'
    DANCE = 'DANCE'
    YOGA = 'YOGA'
    CHOICES = (
        (CROSSFIT, 'Crossfit'),
        (COMBAT, 'Combat'),
        (FITNESS, 'Fitness'),
        (DANCE, 'Dance'),
        (YOGA, 'Yoga'),
    )
    max_length = max(len(x[0]) for x in CHOICES)

    title = models.CharField(
        max_length=30,
        verbose_name='Title of workout',
        validators=(validator_name_only_alphabet_and_space, MinLengthValidator(3, 'Title must contains at least 3 characters'))
    )
    type_of_workout = models.CharField(
        max_length=max_length,
        choices=CHOICES,
        default=FITNESS,
    )
    hour = models.CharField(max_length=10, verbose_name='Starting hour')
    date = models.DateField(verbose_name='Date', blank=True, null=True)
    venue = models.CharField(
        max_length=50,
        verbose_name='Place',
        validators=(
            validator_name_only_alphabet_and_space,
            MinLengthValidator(3, 'Venue must contains at least 3 characters')
        )
    )
    img = models.URLField(blank=True, null=True)
    description = models.TextField(verbose_name='Description')

    participant = models.ManyToManyField(
        UserModel,
        blank=True,
        verbose_name='Participants',
        related_name='participants_of_event'
    )
    team = models.ManyToManyField(
        UserModel,
        verbose_name='Team',
        related_name='team_of_event',
        blank=True
    )

    def __str__(self):
        return self.title