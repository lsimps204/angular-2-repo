from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Recipe
from .filters import UserFilter
from .serializers import (
    RecipeSerializer, 
    RecipeCreateUpdateSerializer, 
    UserSerializer, 
    UserReadSerializer
)

# Lists all recipes
class RecipeListAPIView(generics.ListAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ["name", "description"] # Ordering fields: specified via a query_param
    ordering = ["name"] # Default ordering (no query_param required)
    
    # Return all recipes, or filter by the query parameter
    def get_queryset(self):
        queryset = Recipe.objects.all()
        recipe_name = self.request.query_params.get('name', None)
        if recipe_name is not None:
            queryset = queryset.filter(name__icontains=recipe_name)
        return queryset


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

    # perform_create = a hook provided by CreateAPIView, allowing actions to be performed when the object's created.
    # Here, it was used to hash the user's pw. Now moved into the serializer's 'create' method
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     instance.set_password(instance.password)
    #     instance.save()

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserReadSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    #filter_fields = ['username', 'email'] # Defines simple equality-based filtering, ex: xyz?username=lsimps204&email=abc
    filterset_class = UserFilter # Use custom filter, defined in filters.py
    search_fields = ['username', 'email'] # Allows simple searching using the 'search' query_param