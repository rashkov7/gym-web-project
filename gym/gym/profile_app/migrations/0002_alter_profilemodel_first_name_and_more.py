# Generated by Django 4.0.3 on 2022-04-09 06:39

import django.core.validators
from django.db import migrations, models

from gym.helpers.validators import validate_string_only_alphabet


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(max_length=30, validators=[validate_string_only_alphabet, django.core.validators.MinLengthValidator(3, 'Name must contains at least 3 characters')], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='gender',
            field=models.CharField(choices=[('Do not show', 'Do not show'), ('Male', 'Male'), ('Female', 'Female')], default='Do not show', max_length=11),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(default='Anym', max_length=30, validators=[validate_string_only_alphabet, django.core.validators.MinLengthValidator(3, 'Name must contains at least 3 characters')], verbose_name='Last Name'),
            preserve_default=False,
        ),
    ]
