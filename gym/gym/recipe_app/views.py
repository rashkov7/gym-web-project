from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from gym.recipe_app.forms import RecipeForm, RecipeCommentForm
from gym.recipe_app.models import RecipeModel, CommentRecipeModel


class CreateRecipe(LoginRequiredMixin, CreateView):
    template_name = 'recipes/create_recipe.html'
    model = RecipeModel
    form_class = RecipeForm
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object = form.save(commit=True)
        return super().form_valid(form)


class RecipeListView(ListView, ):
    template_name = 'recipes/recipes-list.html'
    model = RecipeModel
    paginate_by = 3
    ordering = ['-date']


class DetailRecipeView(FormMixin, DetailView):
    template_name = 'recipes/recipe-details.html'
    model = RecipeModel
    form_class = RecipeCommentForm

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['form'] = self.get_form()
        result['comments'] = CommentRecipeModel.objects.filter(recipe_id=self.kwargs['pk'])
        return result


def create_recipe_comment(request, pk):
    recipe = get_object_or_404(RecipeModel, pk=pk)
    user = request.user
    CommentRecipeModel.objects.create(
        text=request.POST['text'],
        owner=user,
        recipe=recipe,
    )
    return redirect('details recipe', pk)


class UpdateRecipeView(UpdateView):
    template_name = 'recipes/edit-recipe.html'
    model = RecipeModel
    fields = ('title', 'description', 'cooking_time', 'servings', 'vegan', 'img')

    def get_success_url(self):
        return reverse_lazy('details recipe', kwargs={'pk': self.object.id})


def delete_recipe(request, pk):
    recipe = RecipeModel.objects.filter(pk=pk)
    recipe.delete()
    return redirect('list recipe')


@login_required(login_url='login')
def like_recipe(request, pk):
    recipe = get_object_or_404(RecipeModel, pk=pk)
    user = request.user
    all_likes = recipe.likes.all()
    if user in all_likes:
        recipe.likes.remove(user)
        return redirect('list recipe')
    recipe.likes.add(request.user)
    return redirect('list recipe')


@login_required(login_url='login')
def add_favorite(request, pk):
    recipe = get_object_or_404(RecipeModel, pk=pk)
    user = request.user
    if recipe:
        if user in recipe.favorites.all():
            recipe.favorites.remove(user)
            return redirect('list recipe')
        else:
            recipe.favorites.add(user)
            return redirect('list recipe')
