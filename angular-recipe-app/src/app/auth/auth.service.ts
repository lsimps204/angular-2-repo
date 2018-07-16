import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Router } from "@angular/router";

export const TOKEN_NAME = "jwt_token"

@Injectable()
export class AuthService {

    private authBase = "http://localhost:8000/api/recipes"

    private user = {}

    constructor(private http: HttpClient, private router: Router) {}

    /* For registration */
    signupUser(username: string, password: string) {
        const url = `${this.authBase}/register`
        this.http.post(url, {'username': username, 'password': password})
            .subscribe(data => this.router.navigate(["/"]))
    }

    /* For login */
    loginUser(username: string, password: string) {
        const url = `${this.authBase}/api-token-auth`
        this.http.post(url, {'username': username, 'password': password})
            .subscribe(data => {
                this.setToken(data['token'])
                this.user = {'username': username }
                this.router.navigate(["/"])
            })
    }

    logout() {
        localStorage.clear()
        this.user = {}
        this.router.navigate(["/"])
    }

    setToken(token: string) {
        localStorage.setItem(TOKEN_NAME, token)
    }

    /* No checks for token's expiration time at the moment */
    getToken() {
        return localStorage.getItem(TOKEN_NAME)
    }

    hasToken() {
        return localStorage.getItem(TOKEN_NAME) !== null
    }

    isAuthenticated() { return this.hasToken() }

    /* Adds the HTTP Authorization header with the JWT */
    createJwtHeaders() {
        return new HttpHeaders({
            'Content-Type': 'application/json',
            'Authorization': `JWT ${this.getToken()}`
        })
    }

}