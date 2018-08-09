from django.conf import settings
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    imagePath = models.URLField(max_length=1024, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('recipe_detail', args=[str(self.pk)])

# Many-to-Many through model.
class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_to_recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_to_ingredient')
    amount = models.IntegerField()