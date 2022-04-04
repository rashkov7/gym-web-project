from django import forms

from gym.recipe_app.models import RecipeModel


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude = ('data', 'author', 'likes','favorites')
