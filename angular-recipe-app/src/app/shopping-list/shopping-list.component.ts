import { Component, OnInit, OnDestroy } from '@angular/core';
import { Ingredient, RecipeIngredient } from '../shared/ingredient.model'
import { ShoppingListService } from './shopping-list.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-shopping-list',
  templateUrl: './shopping-list.component.html',
  styleUrls: ['./shopping-list.component.css'],
})
export class ShoppingListComponent implements OnInit, OnDestroy {

  recipe_ingredients: RecipeIngredient[]
  private subscription: Subscription
  
  constructor(private slService: ShoppingListService) { }

  ngOnInit() {
    this.recipe_ingredients = this.slService.getIngredients();
    this.subscription = this.slService.ingredientsChanged.subscribe( 
      (ingredients:RecipeIngredient[]) => this.recipe_ingredients = ingredients
    )
  }

  ngOnDestroy() {
    this.subscription.unsubscribe()
  }

  onEditItem(index: number) {
    this.slService.startedEditing.next(index)
  }
}
