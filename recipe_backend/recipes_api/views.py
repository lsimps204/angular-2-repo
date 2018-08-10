from django.contrib.auth import get_user_model
from django.views.generic.list import MultipleObjectMixin

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

import os

from .tasks import *
from .permissions import AllowIfNotInDockerContainer
from .models import Recipe, Ingredient
from .filters import UserFilter
from .serializers import (
    RecipeSerializer, 
    UserSerializer, 
    UserReadSerializer,
    IngredientSerializer
)

### Ingredient views
class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'list_ingredients_beginning_with_vowels', 'list_ingredients_beginning_with_consonants']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(methods=['GET'], detail=False)
    def list_ingredients_beginning_with_vowels(self, request):
        data = self.serialize_startswith(vowel=True)
        return Response(data)

    @action(methods=['GET'], detail=False)
    def list_ingredients_beginning_with_consonants(self, request):
        data =self.serialize_startswith(vowel=False)
        return Response(data)

    # Serializes the ingredients based on whether they begin with a vowel or consonant.
    def serialize_startswith(self, vowel=True):
        if vowel:
            qs = Ingredient.objects.filter(name__iregex=r"^[aeiou]")
        else:
            qs = Ingredient.objects.exclude(name__iregex=r"^[aeiou]")
        serializer = self.get_serializer(qs, many=True)
        return serializer.data

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
    serializer_class = RecipeSerializer
    permission_classes = [AllowIfNotInDockerContainer]

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
    permission_classes = [AllowAny]

# Updates an existing Recipe, based on the pk in the URL.
# "RetrieveUpdate" - pre-fills the update form w/ existing data
class RecipeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

# Deletes an existing Recipe, based on the pk in the URL.
class RecipeDeleteAPIView(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

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

class RecipeDeleteAllView(APIView):
    # If in the container, use Celery task. Otherwise, RabbitMQ is not installed locally, thus default to synchronous ORM.
    def get(self, request):
        if os.environ.get('DOCKER_CONTAINER', None) is None:
            Recipe.objects.all().delete()
            return Response()
        else:
            delete_all_recipes.delay()
            return Response()

# Generates new recipes on a GET
class RecipeGenerateView(APIView):
    permission_classes = [AllowIfNotInDockerContainer] # Custom permission
    def get(self, request):
        if os.environ.get('DOCKER_CONTAINER', None) is None:
            from .factories import create_fake_data
            create_fake_data()
            return Response()
        else:
            populate_database.delay()
            return Response()