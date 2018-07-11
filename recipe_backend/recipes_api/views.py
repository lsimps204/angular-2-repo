from rest_framework import generics, viewsets

from .models import Recipe
from .serializers import RecipeSerializer, RecipeCreateUpdateSerializer

# Lists all recipes
class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeCreateAPIView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer

# Lists an individual recipe, determined by the primary-key/id in the URL.
# The model field to filter by can be changed via the 'lookup_field' attribute. Defaults to pk.
class RecipeDetailAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'

# Updates an existing Recipe, based on the pk in the URL.
# "RetrieveUpdate" - pre-fills the update form w/ existing data
class RecipeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    lookup_field = 'pk'

# Deletes an existing Recipe, based on the pk in the URL.
class RecipeDeleteAPIView(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'

 
##### INGREDIENT API ####