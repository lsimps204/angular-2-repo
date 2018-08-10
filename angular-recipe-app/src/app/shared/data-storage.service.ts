import { HttpClient } from "@angular/common/http";
import { RecipeService } from "../recipes/recipe.service";
import { Injectable } from "@angular/core";
import { Recipe } from "../recipes/recipe.model";
import { map } from 'rxjs/operators';
import { AuthService } from "../auth/auth.service";
import { Router } from "@angular/router";
import { Ingredient, RecipeIngredient } from "./ingredient.model";

@Injectable()
export class DataStorageService {

    private baseBackendUrl = "http://localhost:8000/api" // Django or Node backend

    constructor(private http: HttpClient, private recipeService: RecipeService, private authService: AuthService, private router: Router) {}

    /* Gets all the recipes from the backend */
    getRecipes() {
        if (this.authService.hasToken()) {
            const url = `${this.baseBackendUrl}/recipes/`
            return this.http.get<Recipe[]>(url)
            .pipe(
                /* If a given recipe has no ingredients, init an empty array */
                map(recipes => {
                    for (let recipe of recipes) {
                        if (!recipe['recipe_ingredients']) {
                            recipe['recipe_ingredients'] = []
                        }
                    }
                    return recipes
                })
            )
            .subscribe(
                recipes => this.recipeService.setRecipes(recipes)
            )
        } else {
            this.router.navigate(['/signin'])
        }
    }

    /* Stores existing/edited recipes on the backend */
    storeRecipes() {
        const url = `${this.baseBackendUrl}/recipes/create`
        const recipes = this.recipeService.getRecipes()
        return this.http.post<Recipe[]>(url, recipes)
    }


    deleteAllRecipes() {
        if (this.authService.hasToken()) {
            const url = `${this.baseBackendUrl}/recipes/delete`
            this.http.get(url).subscribe(
                res => this.recipeService.setRecipes([]) // Reset the recipes to none
            )
        } else {
            this.router.navigate(["/signin"])
        }
    }

    generateRecipes() {
        if (this.authService.hasToken()) {
            const url = `${this.baseBackendUrl}/recipes/generate`
            this.http.get(url).subscribe()
        } else {
            this.router.navigate(["/signin"])
        }
    }
}