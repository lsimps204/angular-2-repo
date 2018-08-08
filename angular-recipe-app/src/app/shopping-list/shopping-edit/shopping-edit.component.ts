import { Component, OnInit, OnDestroy, ViewChild } from '@angular/core';
import { ShoppingListService } from '../shopping-list.service';
import { Ingredient, RecipeIngredient } from '../../shared/ingredient.model';
import { NgForm } from '@angular/forms';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-shopping-edit',
  templateUrl: './shopping-edit.component.html',
  styleUrls: ['./shopping-edit.component.css']
})
export class ShoppingEditComponent implements OnInit, OnDestroy {

  @ViewChild('f') slForm: NgForm
  subscription: Subscription
  editMode = false
  editedItemIndex: number
  editedItem: RecipeIngredient

  constructor(private slService: ShoppingListService) { }

  ngOnInit() {
    this.subscription = this.slService.startedEditing.subscribe(
      (index: number) => {
        this.editedItemIndex = index
        this.editMode = true
        this.editedItem = this.slService.getIngredient(index)
        this.slForm.setValue({
          name: this.editedItem.ingredient.name,
          amount: this.editedItem.amount
        })
      }
    )
  }

  ngOnDestroy() {
    this.subscription.unsubscribe()
  }

  onSubmitItem(form: NgForm) {
    const value = form.value
    const ingredient = new Ingredient(this.slService.getNextIngredientId(), value.name)
    const amount = value.amount
    const newIngredient = new RecipeIngredient(ingredient, amount)
    if (this.editMode) {
      this.slService.updateIngredient(this.editedItemIndex, newIngredient)
    } else {
      this.slService.addIngredient(newIngredient)
    }
    this.editMode = false
    form.reset()
  }

  onClear() {
    this.editMode = false
    this.slForm.reset()
  }

  onDelete() {
    this.slService.deleteIngredient(this.editedItemIndex)
    this.onClear()
  }

}
