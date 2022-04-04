from django.contrib import admin

# Register your models here.
from gym.recipe_app.models import RecipeModel


@admin.register(RecipeModel)
class AdminRecipe(admin.ModelAdmin):
    pass