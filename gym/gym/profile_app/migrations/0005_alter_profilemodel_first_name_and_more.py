# Generated by Django 4.0.3 on 2022-04-14 18:43

import django.core.validators
from django.db import migrations, models
import gym.helpers.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0004_alter_profilemodel_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[gym.helpers.validators.name_first_letter_validator, gym.helpers.validators.validator_name_only_alphabet_and_space, django.core.validators.MinLengthValidator(3, 'Name must contains at least 3 characters')], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[gym.helpers.validators.validator_name_only_alphabet_and_space, django.core.validators.MinLengthValidator(3, 'Name must contains at least 3 characters')], verbose_name='Last Name'),
        ),
    ]
