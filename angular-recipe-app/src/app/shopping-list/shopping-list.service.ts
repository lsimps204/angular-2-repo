import { Ingredient, RecipeIngredient } from '../shared/ingredient.model'
import { EventEmitter } from '@angular/core';
import { Subject } from 'rxjs';

export class ShoppingListService {

    ingredientsChanged = new Subject<RecipeIngredient[]>()
    startedEditing = new Subject<number>()

    private ingredients: RecipeIngredient[] = [
        new RecipeIngredient(new Ingredient(1, 'Apples'), 5),
        new RecipeIngredient(new Ingredient(2, 'Tomatoes'), 10)
    ]

    getIngredients(): RecipeIngredient[] { 
        return this.ingredients.slice() 
    }
    
    addIngredient(ingredient: RecipeIngredient) {
        if (this.validIngredient(ingredient)) {
            this.ingredients.push(ingredient)
            this.ingredientsChanged.next(this.ingredients.slice())
        }
    }

    addIngredients(ingredients: RecipeIngredient[]) {
        this.ingredients.push(...ingredients) // spread operator (...): spreads the array of ingredients into single ingredients
        this.ingredientsChanged.next(this.ingredients.slice())
    }

    getIngredient(index: number) {
        return this.ingredients[index]
    }

    updateIngredient(index: number, newIngredient: RecipeIngredient) {
        if (this.validIngredient(newIngredient, index)) {
            this.ingredients[index] = newIngredient
            this.ingredientsChanged.next(this.ingredients.slice())
        }
    }

    deleteIngredient(index: number) {
        this.ingredients.splice(index, 1)
        this.ingredientsChanged.next(this.ingredients.slice())
    }

    validIngredient(ingredient: RecipeIngredient, omitIndex: number = -1) {
        let found: number
        if (omitIndex != -1) {
            let filteredList = this.ingredients.filter((v,i) => i != omitIndex)
            found = filteredList.findIndex(val => val.ingredient.name === ingredient.ingredient.name)
        } else {
            found = this.ingredients.findIndex(val => val.ingredient.name === ingredient.ingredient.name)
        }
        console.log(this.ingredients)
        return found == -1
    }

    /* Looks at the list of ingredients and returns the next valid ID */
    public getNextIngredientId() {
        let max_id = 1
        this.ingredients.forEach(recipe_ingredient => {
            max_id = (recipe_ingredient.ingredient.id > max_id) ? recipe_ingredient.ingredient.id : max_id
        })
        return ++max_id
    }
}