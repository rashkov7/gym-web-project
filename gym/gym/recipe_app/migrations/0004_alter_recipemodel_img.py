# Generated by Django 4.0.3 on 2022-04-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_alter_recipemodel_servings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='img',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
