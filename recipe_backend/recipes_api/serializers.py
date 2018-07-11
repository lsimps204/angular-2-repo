from rest_framework import serializers

from .models import Recipe, Ingredient

class IngredientSerializer(serializers.Serializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    # TO DO: fix this to show ingredients list
    #ingredients = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all(), source="ingredients")

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