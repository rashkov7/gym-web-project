from django import forms

from gym.main_app.models import SearchModel
from gym.helpers.mixins import BootstrapFormMixin
from gym.recipe_app.models import RecipeModel, CommentRecipeModel


class RecipeForm(forms.ModelForm, BootstrapFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_placeholder()

    class Meta:
        model = RecipeModel
        exclude = ('data', 'author', 'likes', 'favorites')


class RecipeCommentForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_placeholder()

    class Meta:
        model = CommentRecipeModel
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 2}),
        }


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = '__all__'
