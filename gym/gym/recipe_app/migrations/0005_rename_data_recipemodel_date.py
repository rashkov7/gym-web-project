# Generated by Django 4.0.3 on 2022-04-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0004_remove_recipemodel_prep_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipemodel',
            old_name='data',
            new_name='date',
        ),
    ]
