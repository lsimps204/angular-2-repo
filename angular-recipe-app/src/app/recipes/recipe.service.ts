import { Injectable } from '@angular/core';
import { Recipe } from './recipe.model'
import { Ingredient } from '../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list/shopping-list.service';
import { Subject } from 'rxjs';

@Injectable()
export class RecipeService {
    recipesChanged = new Subject<Recipe[]>()

    private recipes: Recipe[] = [
        new Recipe(
            "Rigatoni Con Pollo e Zucchine", 
            "Pasta and chicken", 
            "https://media-cdn.tripadvisor.com/media/photo-s/09/f4/15/54/rigatoni-con-pollo.jpg",
            [new Ingredient('Chicken', 1), new Ingredient('Pasta', 40)]
        ),
        new Recipe(
            "Salad", 
            "Healthy salad", 
            "http://images.media-allrecipes.com/userphotos/960x960/4552561.jpg",
            [new Ingredient("Tomato", 6), new Ingredient("Peppers", 1), new Ingredient("Red Onion", 1)]
        )
    ]

    constructor(private slService: ShoppingListService ) {}

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