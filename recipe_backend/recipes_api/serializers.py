from rest_framework import serializers

from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    # Nest the serializer to represent a nested relationship.
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'imagePath', 'ingredients']

    # Override init: for setting the 'many' flag on the serializer
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super().__init__(many=many, *args, **kwargs)
        
class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'imagePath', 'ingredients']