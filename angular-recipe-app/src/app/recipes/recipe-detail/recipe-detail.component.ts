import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe.model';
import { RecipeService } from '../recipe.service';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';

@Component({
  selector: 'app-recipe-detail',
  templateUrl: './recipe-detail.component.html',
  styleUrls: ['./recipe-detail.component.css']
})
export class RecipeDetailComponent implements OnInit {

  recipe: Recipe
  id: number

  constructor(
    private recipeService: RecipeService, private route: ActivatedRoute, private router: Router
  ) { }

  /* Subscribe to any changes in the route parameters for this component, and update the recipe accordingly. */
  ngOnInit() {
    this.route.paramMap.subscribe(
      (params: ParamMap) => {
        this.id = +params.get('id')
        if (this.recipeService.recipeExists(this.id)) {
          this.recipe = this.recipeService.getRecipe(this.id)
        } else {
          this.router.navigate(["/recipes"])
        }   
      }
    )
  }

  /* Recipe => Receptas */
  onAddToShoppingList() {
    this.recipeService.addIngredientsToShoppingList(this.recipe.ingredients)
  }

  onEditRecipe() {
    this.router.navigate(['edit'], { relativeTo: this.route })
  }

  onDeleteRecipe() {
    this.recipeService.deleteRecipe(this.id)
    this.router.navigate(["/recipes"])
  }

}
