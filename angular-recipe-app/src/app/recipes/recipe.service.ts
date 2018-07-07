import { EventEmitter, Injectable } from '@angular/core';
import { Recipe } from './recipe.model'
import { Ingredient } from '../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list/shopping-list.service';

@Injectable()
export class RecipeService {
    recipeSelected = new EventEmitter<Recipe>();

    private recipes: Recipe[] = [
        new Recipe(
            "Chicken Curry", 
            "Test Description", 
            "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe_images/recipe-image-legacy-id--488691_11.jpg?itok=ExaTspz1", 
            [new Ingredient('Chicken', 1), new Ingredient('Rice', 40)]
        ),
        new Recipe(
            "Salad", 
            "Healthy salad", 
            "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe_images/recipe-image-legacy-id--488691_11.jpg?itok=ExaTspz1",
            [new Ingredient("Tomato", 6), new Ingredient("Peppers", 1), new Ingredient("Red Onion", 1)]
        )
    ]

    constructor(private slService: ShoppingListService) {}

    getRecipe(index: number): Recipe {
        return this.recipes[index]
    }

    getRecipes(): Recipe[] {
        return this.recipes.slice() // Returns a new array (a copy) of the local recipes array, NOT a reference.
    }

    addIngredientsToShoppingList(ingredients: Ingredient[]) {
        console.log("in service")
        this.slService.addIngredients(ingredients)
    }
}