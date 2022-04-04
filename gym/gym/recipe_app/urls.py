from django.urls import path

from gym.recipe_app.views import CreateRecipe, RecipeListView, like_recipe, add_favorite, DetailRecipeView, \
    UpdateRecipeView,delete_recipe

urlpatterns = (
    path('create/', CreateRecipe.as_view(), name='create recipe'),
    path('list/', RecipeListView.as_view(), name='list recipe'),
    path('like/<int:pk>', like_recipe, name='like recipe'),
    path('fav/<int:pk>', add_favorite, name='favorite recipe'),
    path('details/<int:pk>', DetailRecipeView.as_view(), name='details recipe'),
    path('update/<int:pk>', UpdateRecipeView.as_view(), name='update recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
)