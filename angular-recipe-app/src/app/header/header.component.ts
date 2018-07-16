import { Component } from '@angular/core'
import { DataStorageService } from '../shared/data-storage.service';

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html'
})
export class HeaderComponent {

    constructor(private dsService: DataStorageService) {}

    /* Trigger the GET request to get all recipes */
    onGetData() {
        this.dsService.getRecipes()
    }
    
    /* Trigger the POST request to save all recipes */
    onSaveData() {
        this.dsService.storeRecipes().subscribe(
            data => console.log(data)
        )
    }
}