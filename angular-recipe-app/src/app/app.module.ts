import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'

import { AppComponent } from './app.component';
import { HighlightDirective } from './shared/highlight.directive';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AppRoutingModule } from './app-routing.module';
import { ShoppingListModule } from './shopping-list/shopping-list.module';
import { AuthModule } from './auth/auth.module';
import { CoreModule } from './core/core.module';
import { SignUpGuard } from './auth/signup-guard.service';

@NgModule({
  declarations: [ /* Components, Directives, Pipes */
    AppComponent,
    HighlightDirective,
  ],
  imports: [ /* Which other modules does this module use */
    BrowserModule,
    NgbModule.forRoot(),
    ShoppingListModule,
    AuthModule,
    CoreModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [], /* Which services we use in the module */
  bootstrap: [AppComponent] /* What is the root component */
})
export class AppModule { }