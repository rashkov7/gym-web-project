# Generated by Django 4.0.3 on 2022-04-14 17:34

import django.core.validators
from django.db import migrations, models
import gym.helpers.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_profilemodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(max_length=30, validators=[gym.helpers.validators.name_first_letter_validator, gym.helpers.validators.validator_name_only_alphabet_and_space, django.core.validators.MinLengthValidator(3, 'Name must contains at least 3 characters')], verbose_name='First Name'),
        ),
    ]