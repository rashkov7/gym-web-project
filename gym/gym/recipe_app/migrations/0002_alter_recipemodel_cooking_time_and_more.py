# Generated by Django 4.0.3 on 2022-04-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='cooking_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='prep_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='servings',
            field=models.PositiveIntegerField(default=0),
        ),
    ]