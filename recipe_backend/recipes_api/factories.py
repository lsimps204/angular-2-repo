import factory, random

from .models import *

class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe
        django_get_or_create = ("name",) # Don't duplicate this
    
    name = factory.Faker('name')
    description = factory.Faker('sentence')

class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient
        django_get_or_create = ('name',) # Don't duplicate this
    
    name = factory.Faker('name')

class RecipeIngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RecipeIngredient

    recipe = factory.SubFactory(RecipeFactory)
    ingredient = factory.SubFactory(IngredientFactory)
    amount = random.randint(1,50)

# Creates a recipe with 2 ingredients
class RecipeWithIngredientFactory(RecipeFactory):
    membership = factory.RelatedFactory(RecipeIngredientFactory, 'recipe')
    membership2 = factory.RelatedFactory(RecipeIngredientFactory, 'recipe')


# Create random data:
def create_fake_data():
    for i in range(10):
        RecipeWithIngredientFactory.create()