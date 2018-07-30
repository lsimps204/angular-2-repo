import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from "@angular/router";
import { Injectable } from "@angular/core";
import { AuthService } from "./auth.service";

/* Determines whether the sign up page should be accessible or not.
 * Should be inaccessible when a user is already logged in. 
 */
@Injectable()
export class SignUpGuard implements CanActivate {
    constructor(private authService: AuthService, private router: Router) {}

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
        if (!this.authService.isAuthenticated()) {
            return true
        }
        this.router.navigate(["/"])
        return false
    }
}