from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    imagePath = models.CharField(max_length=1024, blank='')
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.CharField(max_length=128)