from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Recipe
from .serializers import RecipeSerializer, RecipeCreateUpdateSerializer, UserSerializer

# Lists all recipes
class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

class RecipeCreateAPIView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer

    # Override get_serializer to set the serializer's 'many' flag to True if the received data is a list.
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        kwargs['context'] = { 'request': self.request.data }
        return super().get_serializer(*args, **kwargs)


# Lists an individual recipe, determined by the primary-key/id in the URL.
# The model field to filter by can be changed via the 'lookup_field' attribute. Defaults to pk.
class RecipeDetailAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

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

# Registration
class RegisterAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # Override the IsAuthenticated default in settings.py to allow registration