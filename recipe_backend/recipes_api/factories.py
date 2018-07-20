import factory, random
from django.contrib.auth.models import User
from .models import *

class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe
        django_get_or_create = ("name",)
    
    name = factory.Faker('name')
    description = factory.Faker('sentence')

class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient
        django_get_or_create = ('name',)
    
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

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', )

    username = factory.Faker('name')
    email = factory.Faker('ascii_safe_email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

# Run this method to create fake data
def create_fake_data():
    changes_made = False
    if Ingredient.objects.count() < 50:
        [RecipeWithIngredientFactory.create() for _ in range(10)]
        changes_made = True

    if User.objects.count() < 50:
        [UserFactory.create() for _ in range(10)]
        changes_made = True

    return changes_made