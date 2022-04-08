from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class RecipeModel(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    img = models.URLField(null=True, blank=True)
    cooking_time = models.PositiveIntegerField(default=0)
    servings = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    vegan = models.BooleanField(default=False)

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ManyToManyField(UserModel, related_name='recipe_likes', blank=True)
    favorites = models.ManyToManyField(UserModel, default=None, related_name='recipe_favorite', blank=True)

    @property
    def all_likes(self):
        return self.likes.count()

    @property
    def all_favorites(self):
        return self.favorites.count()


class CommentRecipeModel(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)

    @property
    def name_owner(self):
        name = self.owner.profilemodel.full_name
        return name