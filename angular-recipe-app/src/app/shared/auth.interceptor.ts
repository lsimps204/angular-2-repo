import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from "@angular/common/http";
import { Observable } from "rxjs";
import { Injectable } from "@angular/core";
import { AuthService } from "../auth/auth.service";

/* The HttpInterceptor interface requires us to implement an 'intercept' method */
@Injectable()
export class AuthInterceptor implements HttpInterceptor {

    constructor(private authService: AuthService) {}

    /* Sets the JWT for each request to the backend */
    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        //const headers = this.authService.createJwtHeaders()

        const authRequest = request.clone({
            headers: request.headers.set("Authorization", `JWT ${this.authService.getToken()}`)
        })

        return next.handle(authRequest)
    }
}