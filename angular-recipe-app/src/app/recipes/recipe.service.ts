import { Injectable } from '@angular/core';
import { Recipe } from './recipe.model'
import { Ingredient, RecipeIngredient } from '../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list/shopping-list.service';
import { Subject } from 'rxjs';
import { DataStorageService } from '../shared/data-storage.service';

@Injectable()
export class RecipeService {
    recipesChanged = new Subject<Recipe[]>()

    private recipes: Recipe[] = []

    constructor(private slService: ShoppingListService) {}

    setRecipes(recipes: Recipe[]) {
        this.recipes = recipes
        this.recipesChanged.next(this.recipes.slice())
    }

    /* Naive existence check: simply determines if the number passed in is a valid index to this.recipes */
    recipeExists(index: number): boolean {
        return (this.recipes.length - 1) >= index
    }

    getRecipe(index: number): Recipe {
        return this.recipes[index]
    }

    getRecipes(): Recipe[] {
        return this.recipes.slice() // Returns a new array (a copy) of the local recipes array, NOT a reference.
    }

    addIngredientsToShoppingList(ingredients: RecipeIngredient[]) {
        this.slService.addIngredients(ingredients)
    }

    addRecipe(recipe: Recipe) {
        this.recipes.push(recipe)
        this.recipesChanged.next(this.recipes.slice())
    }

    updateRecipe(index: number, newRecipe: Recipe) {
        this.recipes[index] = newRecipe
        this.recipesChanged.next(this.recipes.slice())
    }

    deleteRecipe(index: number) {
        this.recipes.splice(index, 1)
        this.recipesChanged.next(this.recipes.slice())
    }
}