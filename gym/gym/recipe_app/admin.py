from django.contrib import admin

from gym.recipe_app.models import RecipeModel, CommentRecipeModel


@admin.register(RecipeModel)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')


@admin.register(CommentRecipeModel)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('owner', 'recipe', 'date')