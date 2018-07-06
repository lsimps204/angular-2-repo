import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { ShoppingListService } from '../shopping-list.service';
import { Ingredient } from '../../shared/ingredient.model';

@Component({
  selector: 'app-shopping-edit',
  templateUrl: './shopping-edit.component.html',
  styleUrls: ['./shopping-edit.component.css']
})
export class ShoppingEditComponent implements OnInit {

  @ViewChild('nameInput') nameInputRef: ElementRef
  @ViewChild('amountInput') amountInputRef: ElementRef

  constructor(private slService: ShoppingListService) { }

  ngOnInit() {
  }

  onAddItem() {
    const iName = this.nameInputRef.nativeElement.value
    const iAmount = this.amountInputRef.nativeElement.value
    this.slService.addIngredient(new Ingredient(iName, iAmount))
  }

}
