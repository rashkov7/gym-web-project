# Generated by Django 4.0.3 on 2022-04-09 06:39

import django.core.validators
from django.db import migrations, models

from gym.auth_app.validators import validate_string_only_alphabet


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='servings',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator]),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='title',
            field=models.CharField(max_length=30, validators=[validate_string_only_alphabet, django.core.validators.MinLengthValidator(3, 'Title must contains at least 3 characters')], verbose_name='Title'),
        ),
    ]
