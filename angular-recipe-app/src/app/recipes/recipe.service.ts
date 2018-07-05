import { EventEmitter } from '@angular/core';
import { Recipe } from './recipe.model'

export class RecipeService {
    recipeSelected = new EventEmitter<Recipe>();

    private recipes: Recipe[] = [
        new Recipe("Test Recipe", "Test Description", "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe_images/recipe-image-legacy-id--488691_11.jpg?itok=ExaTspz1"),
        new Recipe("Recipe 2", "Delicious Meal", "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe_images/recipe-image-legacy-id--488691_11.jpg?itok=ExaTspz1")
    ]

    getRecipes(): Recipe[] {
        return this.recipes.slice() // Returns a new array (a copy) of the local recipes array, NOT a reference.
    }
}