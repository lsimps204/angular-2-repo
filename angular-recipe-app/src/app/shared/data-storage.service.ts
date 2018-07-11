import { HttpClient } from "@angular/common/http";
import { RecipeService } from "../recipes/recipe.service";
import { Injectable } from "@angular/core";

@Injectable()
export class DataStorageService {

    private baseBackendUrl = "http://localhost:8000/api" // Django or Node backend

    constructor(private http: HttpClient, private recipeService: RecipeService) {}

    getRecipes() {
        const url = `${this.baseBackendUrl}/recipes/`
        return this.http.get(url)
    }
}