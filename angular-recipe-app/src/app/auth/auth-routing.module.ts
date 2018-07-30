import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { SigninComponent } from "./signin/signin.component";
import { SignupComponent } from "./signup/signup.component";
import { SignUpGuard } from "./signup-guard.service";

const authRoutes: Routes = [
    { path: 'signup', component: SignupComponent },
    { path: 'signin', component: SigninComponent, canActivate: [SignUpGuard] },
]

@NgModule({
    imports: [ RouterModule.forChild(authRoutes) ],
    exports: [ RouterModule ],
    providers: [SignUpGuard]
})
export class AuthRoutingModule {

}