from django.urls import path

from gym.recipe_app.views import CreateRecipe, RecipeListView, like_recipe, add_favorite, DetailRecipeView, \
    UpdateRecipeView, delete_recipe, create_recipe_comment

urlpatterns = (

    path('list/', RecipeListView.as_view(), name='list recipe'),
    path('create/', CreateRecipe.as_view(), name='create recipe'),
    path('update/<int:pk>', UpdateRecipeView.as_view(), name='update recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('details/<int:pk>', DetailRecipeView.as_view(), name='details recipe'),

    path('comment/<int:pk>', create_recipe_comment, name='comment recipe'),
    path('like/<int:pk>', like_recipe, name='like recipe'),
    path('fav/<int:pk>', add_favorite, name='favorite recipe'),

)
