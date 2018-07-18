import { NgModule } from "@angular/core";
import { HomeComponent } from "./home/home.component";
import { HeaderComponent } from "./header/header.component";
import { AppRoutingModule } from "../app-routing.module";
import { CommonModule } from "@angular/common";
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { ShoppingListService } from "../shopping-list/shopping-list.service";
import { RecipeService } from "../recipes/recipe.service";
import { DataStorageService } from "../shared/data-storage.service";
import { AuthService } from "../auth/auth.service";
import { AuthGuard } from "../auth/auth-guard.service";

@NgModule({
    declarations: [
        HomeComponent,
        HeaderComponent
    ],
    imports: [
        AppRoutingModule,
        CommonModule,
        NgbModule.forRoot()
    ],
    exports: [
        AppRoutingModule,
        HeaderComponent
    ],
    providers: [ 
        ShoppingListService, 
        RecipeService, 
        DataStorageService, 
        AuthService, 
        AuthGuard 
    ]
})
export class CoreModule {

}