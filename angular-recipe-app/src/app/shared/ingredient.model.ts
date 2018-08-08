export class Ingredient {
    constructor(public id: number = 1, public name: string) {}
}

export class RecipeIngredient {
    constructor(public ingredient: Ingredient, public amount: number) {}
}