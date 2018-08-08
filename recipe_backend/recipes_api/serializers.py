from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Recipe, Ingredient,RecipeIngredient

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['amount']

class IngredientSerializer(serializers.ModelSerializer):
    # See here for potential help:
    # https://github.com/encode/django-rest-framework/issues/5403

    amount = serializers.SerializerMethodField('get_amount_field')

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'amount']

    # TO-DO - find a way to pass the parent recipe here, to filter the return call correctly.
    # Currently throwing a MultipleObjectsFound error.
    def get_amount_field(self, obj):
        try:
            return obj.recipeingredient_set.get(ingredient=obj.pk).amount
        except:
            return ""

class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # Nest the serializer to represent a nested relationship.
    ingredients = IngredientSerializer(many=True, style={'base_template': 'select_multiple.html'})

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'imagePath', 'ingredients']

    # Override the serializer's 'create' method to only create new recipes when no corresponding name and description exists in the database.
    # If they do exist, update instead.
    def create(self, validated_data):
        initial_data = self.context['request'].data # request injected in the view's get_serializer method

        recipe_name = validated_data.get('name', None)
        description = validated_data.get('description', None)
        ingredients = validated_data.get('ingredients', None)
        imagePath = validated_data.get('imagePath', None)

        defaults = { 'imagePath': imagePath }
        recipe, created = Recipe.objects.update_or_create(name=recipe_name, description=description, defaults=defaults)


        # Below: A terrible hack that needs fixed.
        for ingredient in ingredients:
            for ing_name in ingredient.values():
                ing, _ = Ingredient.objects.get_or_create(name=ing_name)

                # Find the recipe, get the amount for the ingredient
                for init in initial_data:
                    if init['name'] == recipe_name:
                        for _ingredient in init['ingredients']:
                            if _ingredient['name'] == ing_name:
                                RecipeIngredient.objects.update_or_create(
                                    amount=_ingredient['amount'],
                                    recipe=recipe,
                                    ingredient=ing
                                )

        return recipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    # Override create to hash the new user's password
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserReadSerializer(serializers.ModelSerializer):
    # Preferable alternative to overriding to_representation to change datetime format
    date_joined = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined']

    # Override to convert date_joined field to more readable output
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['date_joined'] = instance.date_joined.strftime("%d-%m-%Y %H:%M")
    #     return representation