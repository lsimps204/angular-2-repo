import { Injectable } from '@angular/core';
import { Recipe } from './recipe.model'
import { Ingredient } from '../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list/shopping-list.service';

@Injectable()
export class RecipeService {

    private recipes: Recipe[] = [
        new Recipe(
            "Rigatoni Con Pollo e Zucchine", 
            "Pasta and chicken", 
            "data:image/jpeg;base64,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", 
            [new Ingredient('Chicken', 1), new Ingredient('Pasta', 40)]
        ),
        new Recipe(
            "Salad", 
            "Healthy salad", 
            "data:image/jpeg;base64,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",
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