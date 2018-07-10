import { Ingredient } from '../shared/ingredient.model'
import { EventEmitter } from '@angular/core';
import { Subject } from 'rxjs';

export class ShoppingListService {

    ingredientsChanged = new Subject<Ingredient[]>()
    startedEditing = new Subject<number>()

    private ingredients: Ingredient[] = [
        new Ingredient('Apples', 5),
        new Ingredient('Tomatoes', 10)
    ]

    getIngredients() { 
        return this.ingredients.slice() 
    }
    
    addIngredient(ingredient: Ingredient) {
        if (this.validIngredient(ingredient)) {
            this.ingredients.push(ingredient)
            this.ingredientsChanged.next(this.ingredients.slice())
        }
    }

    addIngredients(ingredients: Ingredient[]) {
        this.ingredients.push(...ingredients) // spread operator (...): spreads the array of ingredients into single ingredients
        this.ingredientsChanged.next(this.ingredients.slice())
    }

    getIngredient(index: number) {
        return this.ingredients[index]
    }

    updateIngredient(index: number, newIngredient: Ingredient) {
        if (this.validIngredient(newIngredient, index)) {
            this.ingredients[index] = newIngredient
            this.ingredientsChanged.next(this.ingredients.slice())
        }
    }

    deleteIngredient(index: number) {
        this.ingredients.splice(index, 1)
        this.ingredientsChanged.next(this.ingredients.slice())
    }

    validIngredient(ingredient: Ingredient, omitIndex: number = -1) {
        let found: number
        if (omitIndex != -1) {
            let filteredList = this.ingredients.filter((v,i) => i != omitIndex)
            found = filteredList.findIndex(val => val.name === ingredient.name)
        } else {
            found = this.ingredients.findIndex(val => val.name === ingredient.name)
        }
        console.log(this.ingredients)
        return found == -1
    }
}