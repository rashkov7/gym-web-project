from django import forms

from gym.recipe_app.models import RecipeModel, CommentRecipeModel


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude = ('data', 'author', 'likes','favorites')


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = CommentRecipeModel
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 2}),
        }

    def save(self, commit=True):
        super().save(commit=False)
