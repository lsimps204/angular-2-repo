import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HighlightDirective } from './shared/highlight.directive';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ShoppingListService } from './shopping-list/shopping-list.service';
import { AppRoutingModule } from './app-routing.module';
import { RecipeService } from './recipes/recipe.service';
import { DataStorageService } from './shared/data-storage.service';
import { AuthService } from './auth/auth.service';
import { AuthGuard } from './auth/auth-guard.service';
import { ShoppingListModule } from './shopping-list/shopping-list.module';
import { AuthModule } from './auth/auth.module';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [ /* Components, Directives, Pipes */
    AppComponent,
    HeaderComponent,
    HighlightDirective,
    HomeComponent
  ],
  imports: [ /* Which other modules does this module use */
    BrowserModule,
    NgbModule.forRoot(),
    ShoppingListModule,
    AuthModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [ShoppingListService, RecipeService, DataStorageService, AuthService, AuthGuard ], /* Which services we use in the module */
  bootstrap: [AppComponent] /* What is the root component */
})
export class AppModule { }