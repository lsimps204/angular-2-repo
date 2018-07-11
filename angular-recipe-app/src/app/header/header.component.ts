import { Component } from '@angular/core'
import { DataStorageService } from '../shared/data-storage.service';

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html'
})
export class HeaderComponent {

    constructor(private dsService: DataStorageService) {}

    onGetData() {
        this.dsService.getRecipes().subscribe(
            (response: Response) => console.log(response)
        )
    }
    
}