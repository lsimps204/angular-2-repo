import { Ingredient, RecipeIngredient } from "../shared/ingredient.model";

/* Recipe model */
export class Recipe {
    public name: string
    public description: string
    public imagePath: string
    public recipe_ingredients: RecipeIngredient[]

    constructor(name: string, description: string, imagePath: string, recipe_ingredients: RecipeIngredient[]) {
        this.name = name
        this.description = description
        this.imagePath = imagePath
        this.recipe_ingredients = recipe_ingredients
    }
}